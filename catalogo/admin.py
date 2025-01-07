from django.contrib import admin
from .models import Acabado, Color, Guitarra, Galeria, Carrusel, ImagenCarrusel, Accesorios, TipoMadera  


class AcabadoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_per_page = 10

class ColorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_per_page = 10

class GaleriaInline(admin.StackedInline):
    model = Galeria
    extra = 1
    fields = ('imagen_principal', 'imagen_extra_1', 'imagen_extra_2', 'imagen_extra_3', 'imagen_extra_4')


class GuitarraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre', 'precio')
    list_per_page = 10  
    inlines = [GaleriaInline]

class TipoMaderaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_per_page = 10 

class AccesoriosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre', 'descripcion')
    list_per_page = 10


class ImagenCarruselInline(admin.StackedInline):
    model = ImagenCarrusel
    extra = 1


@admin.register(Carrusel)
class CarruselAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    inlines = [ImagenCarruselInline]


@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('carrusel', 'orden')
    

admin.site.register(Guitarra, GuitarraAdmin)
admin.site.register(TipoMadera, TipoMaderaAdmin)
admin.site.register(Accesorios, AccesoriosAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Acabado, AcabadoAdmin)



