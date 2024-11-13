from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)


    #comentar en caso de necesidad para crear más super usuarios

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[ ]