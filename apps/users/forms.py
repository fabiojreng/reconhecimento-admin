from django import forms
from django.core.exceptions import ValidationError
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "document", "course", "registration_code", "photo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

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
