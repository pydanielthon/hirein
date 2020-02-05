from django.db import models
from django.contrib.auth.models import AbstractUser

#niestandardowy model uzytkownika, umozliwia dodanie dodatkowych pol
class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email