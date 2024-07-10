from django.db import models

class Clases(models.Model):
    clases = models.CharField(max_length=50)
    valor = models.IntegerField()
    
    class Meta:
        verbose_name = ('clase')
        verbose_name_plural = ('clases')
        ordering = ['clases']
    
    def __str__(self):
        return f"{self.clases}" 

class Horario(models.Model):
    horario = models.TimeField()    
    def __str__(self):
        return f"{self.horario}" 
    
class Reserva (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fecha = models.DateField()
    
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
