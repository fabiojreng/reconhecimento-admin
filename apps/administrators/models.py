from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    BaseUserManager,
)
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class Administrator(AbstractBaseUser, PermissionsMixin):
    adminstrator_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Nome")
    password = models.CharField(max_length=128, verbose_name="Senha")
    document = models.CharField(max_length=15, verbose_name="CPF")
    registration_code = models.CharField(
        max_length=45, unique=True, verbose_name="Código de Registro"
    )
    photo = models.ImageField(
        upload_to="admin_photos/", blank=True, verbose_name="Foto"
    )
    key = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    user_permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, related_name="administrators", blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.photo and not self.key:
            self.key = validate_image_key(self.photo.name)
        super().save(*args, **kwargs)
