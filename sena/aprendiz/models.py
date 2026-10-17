from django.db import models

# Create your models here.

class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    ficha = models.CharField(max_length=20, unique=True)
    lugar = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50) 
    modalidad = models.CharField(max_length=50)
    nivel_profesion = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - Ficha: {self.ficha}"

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instructor: {self.nombre} {self.apellido}"

class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
