# Generated by Django 5.1.4 on 2025-01-02 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitarra',
            name='galeria',
        ),
        migrations.AddField(
            model_name='galeria',
            name='guitarra',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.guitarra'),
        ),
    ]