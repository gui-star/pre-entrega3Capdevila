from django import forms

class formSetEstudiante(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class formSetProfesor (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class formSetCurso (forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.CharField(max_length=40)
    horario = forms.CharField(max_length=40)

class formSetEntregable (forms.Form):
    curso = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=40)
    entregada = forms.BooleanField()


class AvatarForm(forms.Form):
    avatar = forms.ImageField()    