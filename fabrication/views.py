from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import FormularioReceta
from . models import Receta
# Create your views here.

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
    data ={'form':form}
    return render(request, 'fabrication.html', data)

def eliminarRecetas(request, id_receta):
    Recetas = Receta.objects.get(id_receta=id_receta)
    form = FormularioReceta(instance=Recetas)
    if(request.method == 'POST'):
        form = FormularioReceta(request.POST, instance=Recetas)
        if(form.is_valid()):
            Recetas.delete()
            return redirect('/')
    data = {'form': form, 'titulo': 'Eliminar'}
    return render(request, 'agregar.html', data)

def editarRecetas(request, id_receta):
    Recetas2 = Receta.objects.all()
    Recetas = Receta.objects.get(id_receta=id_receta)
    form = FormularioReceta(instance=Recetas)
    if(request.method == 'POST'):
        form = FormularioReceta(request.POST, instance=Recetas)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    data = {'form': form, 'titulo': 'Editar', 'Recetas2': Recetas2}
    return render(request, 'agregar.html', data)

def agregarfabricacion(request, id_receta):
    fabricacion = Receta.objects.get(id_receta=id_receta)
    form = FormularioFabricacion(instance=fabricacion)

    codigo = fabricacion.codigo
    existencias = Existencia.objects.get(codigo_Ingreso_NI=codigo)
    e1 = existencias.existencia

    codigo_2 = fabricacion.codigo_2
    codigo_3 = fabricacion.codigo_3
    codigo_4 = fabricacion.codigo_4
    codigo_5 = fabricacion.codigo_5
    codigo_6 = fabricacion.codigo_6
    codigo_7 = fabricacion.codigo_7
    codigo_8 = fabricacion.codigo_8
    codigo_9 = fabricacion.codigo_9
    codigo_10 = fabricacion.codigo_10

    if codigo_2 != None or codigo_2 != None or codigo_2 != None or codigo_2 != None or codigo_2 != None or codigo_2 != None or codigo_2 != None or codigo_2 != None or codigo_2 != None:
        if codigo_2 != None:
            existencias_2 = Existencia.objects.get(codigo_Ingreso_NI=codigo_2)
            e2 = existencias_2.existencia
            data = {'form': form, 'exist1': e1, 'exist2': e2,
                    'titulo': 'Registro', 'nombre': "Fabricación"}

            if codigo_3 != None:
                existencias_3 = Existencia.objects.get(
                    codigo_Ingreso_NI=codigo_3)
                e3 = existencias_3.existencia
                data = {'form': form, 'exist1': e1, 'exist2': e2,
                        'exist3': e3, 'titulo': 'Registro', 'nombre': "Fabricación"}

                if codigo_4 != None:
                    existencias_4 = Existencia.objects.get(
                        codigo_Ingreso_NI=codigo_4)
                    e4 = existencias_4.existencia
                    data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3,
                            'exist4': e4, 'titulo': 'Registro', 'nombre': "Fabricación"}

                    if codigo_5 != None:
                        existencias_5 = Existencia.objects.get(
                            codigo_Ingreso_NI=codigo_5)
                        e5 = existencias_5.existencia
                        data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3,
                                'exist4': e4, 'exist5': e5, 'titulo': 'Registro', 'nombre': "Fabricación"}

                        if codigo_6 != None:
                            existencias_6 = Existencia.objects.get(
                                codigo_Ingreso_NI=codigo_6)
                            e6 = existencias_6.existencia
                            data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4,
                                    'exist5': e5, 'exist6': e6, 'titulo': 'Registro', 'nombre': "Fabricación"}

                            if codigo_7 != None:
                                existencias_7 = Existencia.objects.get(
                                    codigo_Ingreso_NI=codigo_7)
                                e7 = existencias_7.existencia
                                data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                        'exist7': e7, 'titulo': 'Registro', 'nombre': "Fabricación"}

                                if codigo_8 != None:
                                    existencias_8 = Existencia.objects.get(
                                        codigo_Ingreso_NI=codigo_8)
                                    e8 = existencias_8.existencia
                                    data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                            'exist7': e7, 'exist8': e8, 'titulo': 'Registro', 'nombre': "Fabricación"}

                                    if codigo_9 != None:
                                        existencias_9 = Existencia.objects.get(
                                            codigo_Ingreso_NI=codigo_9)
                                        e9 = existencias_9.existencia
                                        data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                                'exist7': e7, 'exist8': e8, 'exist9': e9, 'titulo': 'Registro', 'nombre': "Fabricación"}

                                        if codigo_10 != None:
                                            existencias_10 = Existencia.objects.get(
                                                codigo_Ingreso_NI=codigo_10)
                                            e10 = existencias_10.existencia
                                            data = {'form': form, 'exist1': e1, 'exist2': e2, 'exist3': e3, 'exist4': e4, 'exist5': e5, 'exist6': e6,
                                                    'exist7': e7, 'exist8': e8, 'exist9': e9, 'exist10': e10, 'titulo': 'Registro', 'nombre': "Fabricación"}
    else:
        data = {'form': form, 'exist1': e1, 'titulo': 'Registro', 'nombre': "Fabricación"}

    if(request.method == 'POST'):
        form = FormularioFabricacion(request.POST)
        form.empty_permitted = True
        form.save()
        return redirect('/')
    
    return render(request, 'fabricacion.html', data)

