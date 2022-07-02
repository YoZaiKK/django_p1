from django.db import models 

# Create your models here.
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50) 
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50) 
    descripcion = models.CharField(max_length=100) 
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    categorias = models.ForeignKey(CategoriaProd, on_delete = models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.nombre