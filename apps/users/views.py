from django.shortcuts import render
from .models import User, UserProfile, AdminProfile

# Create your views here.


def crear_partida(request):
    user = request.user
    if User.user:
        profile = User.get_user_profile()
        if profile:
            # Codigo para iniciar partida
            pass
        else:
            # Redireccionar, levantar error, etc
            pass
    else:
        # Redireccionar, levantar error, etc
        pass