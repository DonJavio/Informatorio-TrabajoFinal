from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class User(AbstractUser):
    admin = models.BooleanField(default= False)
    user = models.BooleanField(default=False)

    # Estas funciones nos permiten obtener los perfiles de acuerdo al tipo de usuario en nuestro modelo User.
    def get_admin_profile(self):
        admin_profile = None
        if hasattr(self, 'adminprofile'):
            admin_profile = self.adminprofile
        return admin_profile
    def get_user_profile(self):
        user_profile = None
        if hasattr(self, 'userprofile'):
            user_profile = self.userprofile
        return user_profile 

    class Meta:
        db_table = 'auth_user'
        

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length= 64)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length= 64)
    





