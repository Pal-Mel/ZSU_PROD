from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    phone = models.CharField(max_length=13,blank=True)
    wokrplace = models.CharField(max_length=50)

    def __str__(self):
        return 'Профіль користувача {}'.format(self.user.username)