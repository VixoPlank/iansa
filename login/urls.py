from django.urls import path

# Views
from .views  import *

# Config URL

urlpatterns = [
    path('', login_view.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name ='logout'),
]

