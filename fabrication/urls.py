from django.urls import path


# Views

from . import views

# Config URL

urlpatterns = [
    path('agregar-receta/', views.agregarRecetas, name='agregar-receta'),
]