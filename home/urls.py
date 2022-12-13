from django.urls import path

# Views
from . import views

# Config URL

urlpatterns = [
    path('', views.home, name='home'),
]