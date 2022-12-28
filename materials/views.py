from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioEntradas, FormularioMateria, FormularioMateriaVista
from .models import Materia, Entradas

# Create your views here.

@login_required
def reportes(request):
    materias = Materia.objects.all()
    data = {'materias':materias}
    return render(request, 'reportes.html', data)

@login_required
def menu(request):
    materias = Materia.objects.all()
    data = {'materias':materias}
    return render(request, 'menu.html', data)

@login_required
def agregarMaterias(request):
    form=FormularioMateria()
    if(request.method=='POST'):
        form=FormularioMateria(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/panel-materias/')
    data ={'form':form}
    return render(request, 'registrar.html', data)

@login_required
def agregarentradas(request,id):
    entradas = Entradas.objects.all()
    existencia = Materia.objects.get(codigo=id)
    form=FormularioMateriaVista(instance=existencia)
    form2=FormularioEntradas(instance=existencia)
    if(request.method=='POST'):
        form=FormularioMateriaVista(request.POST,instance=existencia)
        if(form.is_valid()):
            form.save() 
        form2=FormularioEntradas(request.POST)
        if(form2.is_valid()):
            form2.save()
            return redirect('/panel-materias/')
    data ={'form':form,'form2':form2,'titulo':'Agregar','nombre':"Entradas",'entradas':entradas}
    return render(request, 'entradas.html', data)

@login_required
def editarMaterias(request, id):
    materia = Materia.objects.get(codigo = id)
    form2 = FormularioMateriaVista(instance=materia)
    form = FormularioMateria(instance = materia)
    if(request.method == 'POST'):
        form = FormularioMateria(request.POST,instance = materia) #Le entrego los datos a traves del POST
        if(form.is_valid()): #Si es valido los datos los guardo
            form.save()
            return redirect('/panel-materias/')
    data = {'form': form, 'form2':form2}
    return render(request, 'editar.html', data)

@login_required
def eliminarmateria(request, id):
    materia = Materia.objects.get(codigo = id)
    materia.delete()
    return redirect('/panel-materias/')

@login_required
def entradas(request):
    entradas = Entradas.objects.all()
    data = {'entradas':entradas}
    return render(request, 'tabla_entradas.html', data)

