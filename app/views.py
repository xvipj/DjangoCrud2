from django.shortcuts import render, redirect, get_list_or_404
from .models import ExampleModel

# View para la pagina principal
def index(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre") # tomar el valor del input
        photo = request.FILES.get("photo") # tomar el archivo subido

        if not nombre: # si el nombre esta vacio
            return redirect('index') # redirigir a la pagina principal
        
        # crear un objeto en la base de datos 
        object = ExampleModel.objects.create(
            name=nombre,
            photo=photo
        )
        object.save() # guardar el objeto en la base de datos

    all_name = ExampleModel.objects.all()

    contex = {"all_name": all_name }

    return render(request, 'index.html', contex)

# View para eliminar un objeto
def delete(request, pk):
    try:
        object = ExampleModel.objects.get(pk=pk)
        object.delete()
    except ExampleModel.DoesNotExist: # en caso que no exista el objeto
        pass
    return redirect('index')

# View para actualizar un objeto
def update(request, pk):
    nombre = get_list_or_404(ExampleModel, pk=pk)
    if request.method == "POST":

        nombre = request.POST.get("nombre") # tomar el valor del input

        if not nombre: # si el nombre esta vacio
            return redirect('index') # redirigir a la pagina principal

        object = ExampleModel.objects.get(pk=pk) # obtener el objeto de la base de datos
        object.name = nombre
        object.save() # guardar el objeto en la base de datos

        return redirect('index')
    return render(request, 'update.html')