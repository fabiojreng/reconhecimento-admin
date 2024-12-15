from django import forms
from .models import Administrator
from django.contrib.auth.models import Group, Permission


class AdminForm(forms.ModelForm):

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "form-control", "size": "10"}),
    )
    is_active = forms.BooleanField(required=False, initial=True)
    is_staff = forms.BooleanField(required=False, initial=False)
    is_superuser = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Administrator
        fields = [
            "email",
            "name",
            "password",
            "document",
            "registration_code",
            "photo",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        widgets = {
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o email",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite sua senha",
                },
            ),
            "document": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o CPF"}
            ),
            "registration_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite a matrícula"}
            ),
            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")

        print(password)
        if password:
            user.set_password(password)
        elif not password:
            user.password = user.password
        if commit:
            user.save()
        return user


class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control", "size": "10"}),
        required=False,
        label="Permissões",
    )

    class Meta:
        model = Group
        fields = ["name", "permissions"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def save(self, commit=True):
        group = super().save(commit=False)
        if commit:
            group.save()
            group.permissions.set(self.cleaned_data["permissions"])

        return group
