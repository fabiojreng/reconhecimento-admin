# Generated by Django 5.1.4 on 2024-12-13 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0002_rename_adminstrator_id_administrator_administrator_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='key',
        ),
    ]
