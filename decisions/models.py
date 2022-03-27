from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.conf import settings

from core.models import TimestampMixin


class Decision(TimestampMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("decisions:detail", kwargs={"pk": self.pk})


class Option(TimestampMixin):
    decision = models.ForeignKey(
        Decision, related_name="options", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

    def choose(self):
        options = Option.objects.filter(decision=self.decision).exclude(pk=self.pk)
        options.update(is_chosen=False)
        self.is_chosen = True
        self.save()

    def get_score(self):
        pro_sum = self.pros.aggregate(Sum("weight"))["weight__sum"]
        con_sum = self.cons.aggregate(Sum("weight"))["weight__sum"]
        return (pro_sum or 0) - (con_sum or 0)


class Pro(TimestampMixin):
    option = models.ForeignKey(Option, related_name="pros", on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.description


class Con(TimestampMixin):
    option = models.ForeignKey(Option, related_name="cons", on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.description
