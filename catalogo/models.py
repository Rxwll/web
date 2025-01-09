from django.db import models 

class Acabado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoMadera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Accesorios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Bajoquinto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    curvas = models.IntegerField(default=0)

    accesorios = models.ManyToManyField(Accesorios, blank=True) 
    acabado = models.ForeignKey(Acabado, null=True, on_delete=models.CASCADE) 
    color = models.ForeignKey(Color, null=True, on_delete=models.CASCADE) 
    tipo_madera = models.ForeignKey(TipoMadera, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Galeria(models.Model):
    guitarra = models.OneToOneField(Bajoquinto,
            on_delete=models.CASCADE,
            null=True, 
            blank=True
    )

    imagen_principal = models.ImageField(upload_to='productos/principal/', null=True, blank=True)
    imagen_extra_1 = models.ImageField(upload_to='productos/extra/', null=True, blank=True)
    imagen_extra_2 = models.ImageField(upload_to='productos/extra/', null=True, blank=True)
    imagen_extra_3 = models.ImageField(upload_to='productos/extra/', null=True, blank=True)
    imagen_extra_4 = models.ImageField(upload_to='productos/extra/', null=True, blank=True)

    def get_imagenes(self):
        return [
                getattr(self, field.name)
                for field in self._meta.get_fields()
                if field.name.startswith('imagen_') and getattr(self, field.name)
                ]

    def __str__(self):
        return f'Galeria de imagenes de {self.guitarra.nombre}' 


class Carrusel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.nombre


class ImagenCarrusel(models.Model):
    carrusel = models.ForeignKey(Carrusel, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='carrusel/')
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Imagen {self.orden} del carrusel {self.carrusel.nombre}"
