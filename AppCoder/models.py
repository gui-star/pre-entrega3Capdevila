from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.CharField(max_length=40)
    horario = models.CharField(max_length=40)

class Entregable(models.Model):
    curso = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    entregada = models.BooleanField()