from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Disciplina Deportiva")
    # Ej: Fútbol, Tenis, Running, Natación

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    # Ej: Oferta, Profesional, Unisex, Infantil

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Artículo")
    descripcion = models.TextField(verbose_name="Descripción Técnica")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # CAMBIO IMPORTANTE: Campo de imagen
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name="Foto del Producto")
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    dimensiones = models.CharField(max_length=100, help_text="Ej: Talla 42, 70cm diámetro, etc.")
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en Kg (Ej: 0.45 para un balón)")
    
    def __str__(self):
        return f"Detalles técnicos de {self.producto.nombre}"