from django.db import models
from django.contrib.auth.models import AbstractUser

class UserSCATUAZ(AbstractUser):

    materno = models.CharField(
        max_length=50,
    )
    
    def __str__(self):
        return str(self.first_name+' '+self.last_name)