from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.CharField(max_length=30)
    horario = models.CharField(max_length=30)

class Entregable(models.Model):
    curso = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)
    entregada = models.BooleanField()