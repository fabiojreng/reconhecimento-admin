# Generated by Django 5.1.4 on 2024-12-11 17:55

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecognitionLog',
            fields=[
                ('recognition_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('access_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('access_at', models.DateTimeField(auto_now_add=True)),
                ('administrator_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
