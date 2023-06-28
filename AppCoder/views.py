from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Estudiante
from AppCoder.models import Profesor
from AppCoder.models import Curso
from AppCoder.models import Entregable
from AppCoder.forms import *

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario1 = formSetEstudiante(request.POST)
        print(miFormulario1)
        if miFormulario1.is_valid:
            data = miFormulario1.cleaned_data
            estudiante = Estudiante(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
            estudiante.save()
            return render(request,"AppCoder/inicio.html")    
    else:
        miFormulario1 = formSetEstudiante()
    return render(request, "AppCoder/setEstudiantes.html", {"miFormulario1":miFormulario1})

def getEstudiantes(request):
    return render(request, "AppCoder/getEstudiantes.html")

def buscarEstudiante(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getEstudiantes.html", {"estudiantes":estudiantes})
    else:
        respuesta = "No se recibieron los datos"
    
    return HttpResponse(respuesta)

def setProfesores(request):
    if request.method == 'POST':
        miFormulario2 = formSetProfesor(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            data = miFormulario2.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
            profesor.save()
            return render(request,"AppCoder/inicio.html")    
    else:
        miFormulario2 = formSetProfesor()
    return render(request, "AppCoder/setProfesores.html", {"miFormulario2":miFormulario2})

def getProfesores(request):
    return render(request, "AppCoder/getProfesores.html")

def buscarProfesor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getProfesores.html", {"profesores":profesores})
    else:
        respuesta = "No se recibieron los datos"
    
    return HttpResponse(respuesta)

def setCursos(request):
    if request.method == 'POST':
        miFormulario3 = formSetCurso(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid:
            data = miFormulario3.cleaned_data
            curso = Curso(nombre=data["nombre"],camada=data["camada"], horario=data["horario"])    
            curso.save()
            return render(request,"AppCoder/inicio.html")    
    else:
        miFormulario3 = formSetCurso()
    return render(request, "AppCoder/setCursos.html", {"miFormulario3":miFormulario3})

def getCursos(request):
    return render(request, "AppCoder/getCursos.html")

def buscarCurso(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getCursos.html", {"cursos":cursos})
    else:
        respuesta = "No se recibieron los datos"
    
    return HttpResponse(respuesta)

def setEntregables(request):
    if request.method == 'POST':
        miFormulario4 = formSetEntregable(request.POST)
        print(miFormulario4)
        if miFormulario4.is_valid:
            data = miFormulario4.cleaned_data
            entregable = Entregable(curso=data["curso"],fecha=data["fecha"], entregada=data["entregada"])    
            entregable.save()
            return render(request,"AppCoder/inicio.html")    
    else:
        miFormulario4 = formSetEntregable()
    return render(request, "AppCoder/setEntregables.html", {"miFormulario4":miFormulario4})

def getEntregables(request):
    return render(request, "AppCoder/getEntregables.html")

def buscarEntregable(request):
    if request.GET["curso"]:
        curso = request.GET["curso"]
        entregables = Entregable.objects.filter(curso = curso)
        return render(request, "AppCoder/getEntregables.html", {"entregables":entregables})
    else:
        respuesta = "No se recibieron los datos"
    
    return HttpResponse(respuesta)