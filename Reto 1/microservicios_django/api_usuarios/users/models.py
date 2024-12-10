from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    edad = models.IntegerField()
    nombre_cuenta = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    class Meta:
        db_table = 'usuarios'