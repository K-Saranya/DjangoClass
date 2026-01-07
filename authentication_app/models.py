from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UsersOtherInformation(AbstractUser):
    user_city = models.CharField(max_length=50)
    user_pincode = models.IntegerField()
    
    def __str__(self):
        return self.username