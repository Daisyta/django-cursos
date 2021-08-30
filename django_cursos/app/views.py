from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Curso

# una vez que se añaden cursos,hay que mostrarlos en una lista en el mismo template,a traves de un contexto
# se van juntando aca dentro del context
def index(request):
    if request.method == "GET":
        context = {
            "cursos": Curso.objects.all(),
        }
        return render(request, "index.html", context)

    # cuando el usuario crea un curso,puede salir un error o puede salir un registro exitoso ,etc.html', context
    # por lo que se configuran los errores primero'
    if request.method == "POST":
        print("el post del index", request.POST)
        errors = Curso.objects.validaciones(request.POST)

        # aqui se cargan los popup,mensajes de aviso,si hay error
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)

            return redirect("/")
        # si no hay errores,se crea el curso
        else:

            curso = Curso.objects.create(
                Name=request.POST["Name"],
                Description=request.POST["Description"],
            )
            # el mensaje de popup cuando se cree el curso,y se mostrara con el toastr
            messages.success(
                request, f"El curso {curso.Name} ha sido creado correctamente"
            )
            return redirect("/")


def add(request):
    context = {}
    # Tambien se puede redirigir a principal o display
    return render(request, "add.html", context)


def display(request, id):
    context = {"id": id}
    return render(request, "display.html", context)


def edit(request, id):
    context = {"id": id}
    return render(request, "edit.html", context)


def destroy(request, id):
    if request.method == "GET":
        context = {
            "curso" : Curso.objects.get(id=id)
        }
        return render(request, "destroy.html", context)

    if request.method == "POST":
        print("post del destroy", request.POST, id)

        curso = Curso.objects.get(id=id)
        curso.delete()

        messages.info(request,f"El curso {curso.Name} fué eliminado")
        return redirect(f"/")


def destroy_ajax(request,id):
        curso = Curso.objects.get(id=id)
        curso.delete()

        context = {
        "Name" : curso.Name,
        "Description" : curso.Description,
        
        }

        return JsonResponse(context)



def other(request, id):
    context = {"id": id}
    return render(request, "other.html", context)
