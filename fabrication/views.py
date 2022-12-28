from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import FormularioReceta,FormularioFabricacion
from . models import Receta
from materials.models import Materia
# Create your views here.
@login_required
def menu(request):
    recetas = Receta.objects.all()
    data = {'recetas':recetas}
    return render(request, 'menu_receta.html', data)

@login_required
def agregarRecetas(request):
    form=FormularioReceta()
    if(request.method=='POST'):
        form=FormularioReceta(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/agregar-receta/')
    data ={'form':form, 'titulo': 'Registro'}
    return render(request, 'agregar.html', data)

@login_required
def eliminarRecetas(request, id_receta):
    Recetas = Receta.objects.get(id_receta=id_receta)
    form = FormularioReceta(instance=Recetas)
    if(request.method == 'POST'):
        form = FormularioReceta(request.POST, instance=Recetas)
        if(form.is_valid()):
            Recetas.delete()
            return redirect('/agregar-receta')
    data = {'form': form, 'titulo': 'Eliminar'}
    return render(request, 'agregar.html', data)

@login_required
def editarRecetas(request, id_receta):
    Recetas = Receta.objects.get(id_receta=id_receta)
    form = FormularioReceta(instance=Recetas)
    if(request.method == 'POST'):
        form = FormularioReceta(request.POST, instance=Recetas)
        if(form.is_valid()):
            form.save()
            return redirect('/agregar-receta')
    data = {'form': form, 'titulo': 'Editar'}
    return render(request, 'agregar.html', data)

@login_required
def agregarfabricacion(request, id_receta):
    fabricacion = Receta.objects.get(id_receta=id_receta)
    form = FormularioFabricacion(instance=fabricacion)

    codigo_1 = fabricacion.codigo_1
    a = Materia.objects.filter(codigo=codigo_1).first()
    a2 = Materia.objects.filter(codigo=codigo_1).first()
    a3 = Materia.objects.filter(codigo=codigo_1).first()
    a4 = Materia.objects.filter(codigo=codigo_1).first()
    a5 = Materia.objects.filter(codigo=codigo_1).first()
    a6 = Materia.objects.filter(codigo=codigo_1).first()
    a7 = Materia.objects.filter(codigo=codigo_1).first()
    a8 = Materia.objects.filter(codigo=codigo_1).first()
    a9 = Materia.objects.filter(codigo=codigo_1).first()
    a10 = Materia.objects.filter(codigo=codigo_1).first()
    if a != None:
        if codigo_1 != None:
            Materias = Materia.objects.get(codigo=codigo_1)
            e1 = Materias.existencia
            data = {'form': form,'exist1': e1, 'titulo': 'Registro', 'nombre': "Fabricación"}
    
    
    codigo_2 = fabricacion.codigo_2
    codigo_3 = fabricacion.codigo_3
    codigo_4 = fabricacion.codigo_4
    codigo_5 = fabricacion.codigo_5
    codigo_6 = fabricacion.codigo_6
    codigo_7 = fabricacion.codigo_7
    codigo_8 = fabricacion.codigo_8
    codigo_9 = fabricacion.codigo_9
    codigo_10 = fabricacion.codigo_10

    if a2 != None or a3 != None or a4 != None or a5 != None or a6 != None or a7 != None or a8 != None or a9 != None or a10 != None:
        if codigo_2 != None:
            Materias_2 = Materia.objects.get(codigo=codigo_2)
            e2 = Materias_2.existencia
            data = {'form': form,'exist1': e1, 'exist2': e2,
                    'titulo': 'Registro', 'nombre': "Fabricación"}

            if codigo_3 != None:
                Materias_3 = Materia.objects.get(
                    codigo=codigo_3)
                e3 = Materias_3.existencia
                data = {'form': form, 'exist1': e1, 'exist2': e2,
                        'exist3': e3, 'titulo': 'Registro', 'nombre': "Fabricación"}

                if codigo_4 != None:
                    Materias_4 = Materia.objects.get(
                        codigo=codigo_4)
                    e4 = Materias_4.existencia
                    data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3,
                            'exist4': e4, 'titulo': 'Registro', 'nombre': "Fabricación"}

                    if codigo_5 != None:
                        Materias_5 = Materia.objects.get(
                            codigo=codigo_5)
                        e5 = Materias_5.existencia
                        data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3,
                                'exist4': e4, 'exist5': e5, 'titulo': 'Registro', 'nombre': "Fabricación"}

                        if codigo_6 != None:
                            Materias_6 = Materia.objects.get(
                                codigo=codigo_6)
                            e6 = Materias_6.existencia
                            data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4,
                                    'exist5': e5, 'exist6': e6, 'titulo': 'Registro', 'nombre': "Fabricación"}

                            if codigo_7 != None:
                                Materias_7 = Materia.objects.get(
                                    codigo=codigo_7)
                                e7 = Materias_7.existencia
                                data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                        'exist7': e7, 'titulo': 'Registro', 'nombre': "Fabricación"}

                                if codigo_8 != None:
                                    Materias_8 = Materia.objects.get(
                                        codigo=codigo_8)
                                    e8 = Materias_8.existencia
                                    data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                            'exist7': e7, 'exist8': e8, 'titulo': 'Registro', 'nombre': "Fabricación"}

                                    if codigo_9 != None:
                                        Materias_9 = Materia.objects.get(
                                            codigo=codigo_9)
                                        e9 = Materias_9.existencia
                                        data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                                'exist7': e7, 'exist8': e8, 'exist9': e9, 'titulo': 'Registro', 'nombre': "Fabricación"}

                                        if codigo_10 != None:
                                            Materias_10 = Materia.objects.get(
                                                codigo=codigo_10)
                                            e10 = Materias_10.existencia
                                            data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                                    'exist7': e7, 'exist8': e8, 'exist9': e9, 'exist10': e10, 'titulo': 'Registro', 'nombre': "Fabricación"}
    
    else:
        data = {'form': form,'titulo': 'Registro', 'nombre': "Fabricación"}
    if(request.method == 'POST'):
        form = FormularioFabricacion(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/agregar-receta')
    
    return render(request, 'fabricacion.html', data)

