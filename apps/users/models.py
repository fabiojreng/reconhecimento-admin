from django.db import models
import re
import uuid
from django.core.exceptions import ValidationError
from apps.programs.models import Program


def validate_image_key(image_path):
    match = re.search(r"([^/]+)(?=\.[^.]+$)", image_path)
    return match.group(0) if match else None


def validate_image_size(image):
    MAX_SIZE = 5 * 1024 * 1024
    if image.size > MAX_SIZE:
        raise ValidationError("A imagem deve ter no máximo 5 MB.")


def validate_cpf(cpf):

    cpf = re.sub(r"[^0-9]", "", cpf)

    if len(cpf) != 11:
        raise ValidationError("CPF deve ter 11 dígitos.")

    if cpf == cpf[0] * len(cpf):
        raise ValidationError("CPF inválido.")

    def calcular_dv(cpf, peso):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf, peso))
        resto = soma % 11
        if resto < 2:
            return 0
        return 11 - resto

    peso1 = list(range(10, 1, -1))
    dv1 = calcular_dv(cpf[:9], peso1)

    peso2 = list(range(11, 1, -1))
    dv2 = calcular_dv(cpf[:10], peso2)

    if int(cpf[9]) != dv1 or int(cpf[10]) != dv2:
        raise ValidationError("CPF inválido.")

    return cpf


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, verbose_name="Nome")
    document = models.CharField(
        unique=True,
        max_length=15,
        verbose_name="CPF",
        validators=[validate_cpf],
    )

    course = models.CharField(max_length=45, verbose_name="Curso")
    registration_code = models.CharField(
        unique=True, max_length=45, verbose_name="Código de Matrícula"
    )
    photo = models.ImageField(
        upload_to="user_photos/", validators=[validate_image_size], verbose_name="Foto"
    )
    key = models.CharField(
        unique=True, max_length=100, blank=True, verbose_name="Chave da Imagem"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, related_name="users"
    )

    def save(self, *args, **kwargs):
        if self.photo and not self.key:
            self.key = validate_image_key(self.photo.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
