from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('entregables/', entregables,name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('setEstudiante/', setEstudiantes, name="setEstudiante"),
    path('getEstudiante/', getEstudiantes, name="getEstudiante"),
    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),
    path('setProfesor/', setProfesores, name="setProfesor"),
    path('getProfesor/', getProfesores, name="getProfesor"),
    path('buscarProfesor/', buscarProfesor, name="buscarProfesor"),
    path('setCurso/', setCursos, name="setCurso"),
    path('getCurso/', getCursos, name="getCurso"),
    path('buscarCurso/', buscarCurso, name="buscarCurso"),
    path('setEntregable/', setEntregables, name="setEntregable"),
    path('getEntregable/', getEntregables, name="getEntregable"),
    path('buscarEntregable/', buscarEntregable, name="buscarEntregable"),
    path('login/', loginWeb, name="login"),
    path('registro/', registro, name="registro"),
    path('Logout/',LogoutView.as_view(template_name = 'AppCoder/login.html'), name="Logout"),
    path('perfil/', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('AcercaDeMi/', AcercaDeMi, name="AcercaDeMi"),
]