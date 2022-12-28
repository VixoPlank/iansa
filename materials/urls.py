from django.urls import path


# Views
from . import views

# Config URL

urlpatterns = [
    path('', views.menu, name='menu-materias'),
    path('registrar-materias/', views.agregarMaterias, name='registrar-materias'),
    path('entradas-materias/<int:id>', views.agregarentradas, name=' entradas-materias'),
    path('editar-materias/<int:id>', views.editarMaterias, name = 'editar-materias'),
    path('eliminar-materias/<int:id>', views.eliminarmateria, name = 'eliminar-materias'),
    path('reportes-materias/', views.eliminarmateria, name = 'reportes-materias'),
    path('tabla-entradas/', views.entradas, name = 'tabla-entradas'),
    # Reporte
    path('reportes/', views.reportes, name = 'reportes'),
]