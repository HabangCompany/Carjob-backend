from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#일반 회원
class User(AbstractUser):
    address = models.CharField(max_length = 50)
    phonenumber = models.CharField(max_length = 16, null=True)

    def __str__(self):
        """A string representation of the model."""
        return self.username

#업체회원
class Store(User):
    pass