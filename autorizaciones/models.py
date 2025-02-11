from django.db import models
from django.utils import timezone

class Autorizacion(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    fecha_emision = models.DateField(auto_now_add=True)
    vigente = models.BooleanField(default=True)

    def __str__(self):
        return f"Autorización {self.numero}"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    autorizacion = models.OneToOneField(Autorizacion, on_delete=models.CASCADE, null=True, blank=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def aprobar(self):
        if not self.aprobado and self.autorizacion:
            # Verifica que la autorización no haya sido usada antes
            if not Proyecto.objects.filter(autorizacion=self.autorizacion, aprobado=True).exists():
                self.aprobado = True
                self.save()
            else:
                raise ValueError("La autorización ya ha aprobado otro proyecto.")



class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    cid = models.CharField(max_length=20, unique=True)  # ID único
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Teléfono opcional
    proyectos = models.ManyToManyField('Proyecto', related_name='municipios', blank=True)  # Relación con proyectos

    def __str__(self):
        return self.nombre
    
from django.db import models

class Condicion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE, related_name='condiciones')
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, related_name='condiciones')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

