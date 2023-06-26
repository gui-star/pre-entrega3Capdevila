from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola! puedes ingresar a nuestro sitio aquí http://127.0.0.1:8000/AppCoder/inicio/ ")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Mi primer proyecto con Django</h1>")

def miNombreEs(request, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(request):
    nombre = "Natalia"
    apellido = "Chehda"

    namelist = ["Natalia", "Alumno1", "Alumno2", "Alumno3", "Alumno4"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
