from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import FormularioReceta
# Create your views here.

@login_required
def agregarRecetas(request):
    form=FormularioReceta()
    if(request.method=='POST'):
        form=FormularioReceta(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/home/receta/')
    data ={'form':form}
    return render(request, 'fabrication.html', data)