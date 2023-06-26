from django import forms

class formSetEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class formSetProfesor (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class formSetCurso (forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.CharField(max_length=30)
    horario = forms.CharField(max_length=30)

class formSetEntregable (forms.Form):
    curso = forms.CharField(max_length=30)
    fecha = forms.CharField(max_length=30)
    entregada = forms.BooleanField()