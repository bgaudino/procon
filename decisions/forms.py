from tkinter.ttk import Style
from django import forms

from .models import Decision, Option, Pro, Con


class DecisionForm(forms.ModelForm):
    class Meta:
        model = Decision
        fields = ["title", "description"]
        writeonly_fields = ["user"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "input is-primary", "placeholder": "Add a decision"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea is-primary",
                    "placeholder": "Add a description",
                }
            ),
        }


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["title", "description"]
        writeonly_fields = ["decision"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "input is-primary", "placeholder": "Add an option..."}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea is-primary",
                    "placeholder": "Add a description...",
                }
            ),
        }


class ProForm(forms.ModelForm):
    class Meta:
        model = Pro
        fields = ["description", "weight"]
        writeonly_fields = ["option"]
        widgets = {
            "description": forms.TextInput(
                attrs={"class": "input is-success", "placeholder": "Add a pro..."}
            ),
            "weight": forms.NumberInput(
                attrs={
                    "class": "input is-success",
                    "initial": "1",
                }
            ),
        }


class ConForm(forms.ModelForm):
    class Meta:
        model = Con
        fields = ["description", "weight"]
        writeonly_fields = ["option"]
        widgets = {
            "description": forms.TextInput(
                attrs={"class": "input is-danger", "placeholder": "Add a con..."}
            ),
            "weight": forms.NumberInput(
                attrs={
                    "class": "input is-danger",
                    "initial": "1",
                }
            ),
        }
