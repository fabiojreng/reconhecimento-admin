# Generated by Django 5.1.4 on 2024-12-11 17:11

import apps.users.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, verbose_name='Nome')),
                ('document', models.CharField(max_length=15, unique=True, validators=[apps.users.models.validate_cpf], verbose_name='CPF')),
                ('course', models.CharField(max_length=45, verbose_name='Curso')),
                ('registration_code', models.CharField(max_length=45, unique=True, verbose_name='Código de Matrícula')),
                ('photo', models.ImageField(upload_to='user_photos/', validators=[apps.users.models.validate_image_size], verbose_name='Foto')),
                ('key', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Chave da Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='programs.program')),
            ],
        ),
    ]
