# Generated by Django 5.1.4 on 2025-01-06 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Maderas',
            new_name='TipoMadera',
        ),
        migrations.RenameField(
            model_name='guitarra',
            old_name='maderas',
            new_name='tipo_madera',
        ),
    ]
