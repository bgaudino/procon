from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Decision, Option, Pro, Con
from .forms import DecisionForm, OptionForm, ProForm, ConForm
from core.views import ProtectedView


class DecisionView(ProtectedView, generic.ListView):
    model = Decision
    context_object_name = "decisions"
    template_name = "decisions/index.html"
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return (
                Decision.objects.filter(user=user)
                .prefetch_related("options", "options__pros", "options__cons")
                .order_by("-created_at")
            )
        return Decision.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DecisionForm()
        return context


class DecisionDetailView(ProtectedView, generic.DetailView):
    model = Decision
    context_object_name = "decision"
    template_name = "decisions/detail.html"

    def get_object(self, queryset=None):
        decision = get_object_or_404(Decision, pk=self.kwargs["pk"])
        return decision

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["option_form"] = OptionForm()
        context["pro_form"] = ProForm()
        context["con_form"] = ConForm()
        return context


class NewDecisionView(ProtectedView, generic.CreateView):
    model = Decision
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class NewOptionView(ProtectedView, generic.CreateView):
    model = Option
    fields = ["decision", "title", "description"]
    template_name = "decisions/index.html"

    def get_success_url(self):
        return self.object.decision.get_absolute_url()


class NewProView(ProtectedView, generic.CreateView):
    model = Pro
    fields = ["option", "description", "weight"]

    def get_success_url(self):
        return self.object.option.decision.get_absolute_url()


class NewConView(ProtectedView, generic.CreateView):
    model = Con
    fields = ["option", "description", "weight"]

    def get_success_url(self):
        return self.object.option.decision.get_absolute_url()


class DecisionDeleteView(ProtectedView, generic.DeleteView):
    model = Decision
    template_name = "decisions/delete.html"

    def get_success_url(self):
        return reverse("decisions:index")


class OptionDeleteView(ProtectedView, generic.DeleteView):
    model = Option
    template_name = "decisions/delete.html"

    def get_success_url(self):
        return self.object.decision.get_absolute_url()


class ProDeleteView(ProtectedView, generic.DeleteView):
    model = Pro
    template_name = "decisions/delete.html"

    def get_success_url(self):
        return self.object.option.decision.get_absolute_url()


class ConDeleteView(ProtectedView, generic.DeleteView):
    model = Con
    template_name = "decisions/delete.html"

    def get_success_url(self):
        return self.object.option.decision.get_absolute_url()


class DecisionUpdateView(ProtectedView, generic.UpdateView):
    model = Decision
    fields = ["title", "description"]
    template_name = "decisions/update.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse("decisions:update", kwargs={"pk": self.object.pk})
        return context


class OptionUpdateView(ProtectedView, generic.UpdateView):
    model = Option
    fields = ["title", "description"]
    template_name = "decisions/update.html"

    def get_success_url(self):
        return self.object.decision.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse(
            "decisions:options_update", kwargs={"pk": self.object.pk}
        )
        return context


class ProUpdateView(ProtectedView, generic.UpdateView):
    model = Pro
    fields = ["description", "weight"]
    template_name = "decisions/update.html"

    def get_success_url(self):
        return self.object.option.decision.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse(
            "decisions:pros_update", kwargs={"pk": self.object.pk}
        )
        return context


class ConUpdateView(ProtectedView, generic.UpdateView):
    model = Con
    fields = ["description", "weight"]
    template_name = "decisions/update.html"

    def get_success_url(self):
        return self.object.option.decision.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse(
            "decisions:cons_update", kwargs={"pk": self.object.pk}
        )
        return context
