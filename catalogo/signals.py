from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Guitarra, Maderas, Accesorios


# @receiver(post_save, sender=Guitarra)
# def set_defaults(sender, instance, created, **kwargs):
#     if created:
#         default_madera = Maderas.objects.get(nombre='abeto')
#         instance.maderas = default_madera
#         instance.save()
#
#
#     if not instance.accesorios.all():
#         default_accesorio = Accesorios.objects.filter(nombre__in=["Varilla de ajuste", "Trastes", "Huesos", "Cuerdas", "Clavijas"])
#         instance.accesorios.add(default_accesorio)
#         instance.save()
