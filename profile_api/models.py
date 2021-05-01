from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de usuario. Sirve para crear usuarios desde la linea de comandos """

    def create_user(self, email, name, password=None):
        """ Crear un nuevo User Profile """

        if not email:
            raise ValueError('Usuario debe de tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


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
