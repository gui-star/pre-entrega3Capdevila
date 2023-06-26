from django.http import HttpResponse

def saludo(request):
    mensaje = 'Hola! Puedes ingresar a nuestro sitio <a href="http://127.0.0.1:8000/AppCoder/inicio/">aquí</a>.'
    return HttpResponse(mensaje)

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
