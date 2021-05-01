from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo de usuarios del sistema """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Establecemos que el usuario haga login con email y no con username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Obtener nombre completo del usuario """
        return self.name

    def get_short_name(self):
        """ Obtener nombre corto del usuario """
        return self.name

    def __str__(self):
        """ Retornar cadena representando nuestro usuario """
        return self.email
