from django.urls import path


# Views

from . import views

# Config URL

urlpatterns = [
    path('', views.menu, name='menu-recetas'),
    path('agregar-receta', views.agregarRecetas, name='agregar-receta'),
    path('fabricacion-receta/<int:id>', views.agregarentradas, name='fabricacion-receta'),
    path('editar-receta/<int:id>', views.editarreceta, name = 'editar-receta'),
    path('eliminar-receta/<int:id>', views.eliminarmateria, name = 'eliminar-receta'),
]
