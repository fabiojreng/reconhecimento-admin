from django import forms
from django.core.exceptions import ValidationError
from .models import User
from ..administrators.models import Administrator
from ..programs.models import Program


class UserForm(forms.ModelForm):
    program = forms.ModelChoiceField(
        queryset=Program.objects.all(),
        empty_label="Selecione um programa",
        label="Programa",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "document",
            "registration_code",
            "course",
            "photo",
            "program",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome do usuário",
                }
            ),
            "document": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o CPF"}
            ),
            "registration_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite a matrícula"}
            ),
            "course": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o curso"}
            ),
            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def clean_document(self):
        document = self.cleaned_data.get("document")

        if self.instance.pk:
            if (
                User.objects.exclude(pk=self.instance.pk)
                .filter(document=document)
                .exists()
                or Administrator.objects.filter(document=document).exists()
            ):
                raise ValidationError(
                    "Este CPF já está cadastrado em outro usuário ou administrador."
                )
        else:
            if (
                User.objects.filter(document=document).exists()
                or Administrator.objects.filter(document=document).exists()
            ):
                raise ValidationError(
                    "Este CPF já está cadastrado em outro usuário ou administrador."
                )
        return document

    def clean_registration_code(self):
        registration_code = self.cleaned_data.get("registration_code")

        if self.instance.pk:
            if (
                User.objects.exclude(pk=self.instance.pk)
                .filter(registration_code=registration_code)
                .exists()
                or Administrator.objects.filter(
                    registration_code=registration_code
                ).exists()
            ):
                raise ValidationError(
                    "Este código de matrícula já está cadastrado em outro usuário ou administrador."
                )
        else:
            if (
                User.objects.filter(registration_code=registration_code).exists()
                or Administrator.objects.filter(
                    registration_code=registration_code
                ).exists()
            ):
                raise ValidationError(
                    "Este código de matrícula já está cadastrado em outro usuário ou administrador."
                )
        return registration_code
