from django.contrib import admin

from .models import Decision, Option, Pro, Con


class ProInline(admin.StackedInline):
    model = Pro
    extra = 0


class ConInline(admin.StackedInline):
    model = Con
    extra = 0


class OptionInline(admin.StackedInline):
    model = Option
    extra = 0


class DecisionAdmin(admin.ModelAdmin):
    inlines = (OptionInline,)
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)


class OptionAdmin(admin.ModelAdmin):
    inlines = (
        ProInline,
        ConInline,
    )
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)


admin.site.register(Decision, DecisionAdmin)
admin.site.register(Option, OptionAdmin)
