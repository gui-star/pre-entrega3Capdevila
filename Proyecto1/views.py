from django.http import HttpResponse

def saludo(request):
    mensaje = 'Ingresa pulsando <a href="http://127.0.0.1:8000/AppCoder/inicio/">aquí</a>.'
    return HttpResponse(mensaje)

def miNombreEs(request, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(data)

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Mi primer proyecto con Django</h1>")

def probandoTemplate(request):
    apellido = "Capdevila"
    nombre = "Guillermo"

    namelist = ["Guillermo", "Estudiante1", "Estudiante2", "Estudiante3", ]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
