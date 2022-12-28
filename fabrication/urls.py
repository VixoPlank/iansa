from django.urls import path


# Views

from . import views

# Config URL

urlpatterns = [
    path('', views.menu, name='menu-recetas'),
    path('agregar-receta', views.agregarRecetas, name='agregar-receta'),
    path('fabricacion-receta/<int:id_receta>', views.agregarfabricacion, name='fabricacion-receta'),
    path('editar-receta/<int:id_receta>', views.editarRecetas, name = 'editar-receta'),
    path('eliminar-receta/<int:id_receta>', views.eliminarRecetas, name = 'eliminar-receta'),
    
]
