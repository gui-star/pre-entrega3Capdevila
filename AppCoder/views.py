from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Profesor
from AppCoder.models import Curso
from AppCoder.models import Entregable
from AppCoder.forms import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from AppCoder.forms import formSetEstudiante
from AppCoder.forms import AvatarForm
from AppCoder.models import Estudiante, Avatar

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

def AcercaDeMi(request):
    return render(request, 'AppCoder/AcercaDeMi.html')  

def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario1 = formSetEstudiante(request.POST)
        print(miFormulario1)
        if miFormulario1.is_valid():
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

def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("../inicio")
        else:
            return render(request, 'AppCoder/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'AppCoder/login.html')

def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate.is_valid():
            user = userCreate.save(commit=False) 
            user.save()  
            return render(request, 'AppCoder/login.html')
    else:
        userCreate = UserCreationForm()
    return render(request, 'AppCoder/registro.html', {'form': userCreate})

@login_required  
def perfilview(request):
    return render(request, 'AppCoder/Perfil/Perfil.html')

@login_required  
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'AppCoder/Perfil/Perfil.html')
    else:
        form = UserEditForm(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'AppCoder/Perfil/editarPerfil.html', {"form": form})

@login_required
def changePassword(request):
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            else:
                return HttpResponse("Las constraseñas no coinciden")
        return render(request, "AppCoder/inicio.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'AppCoder/Perfil/changePassword.html', {"form": form})
    
def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "AppCoder/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "AppCoder/Perfil/avatar.html", {'form': form})

def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar    

  
