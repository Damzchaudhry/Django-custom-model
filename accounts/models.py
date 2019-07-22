from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	name = models.CharField(blank=True, max_length=255)
	email=models.CharField(max_length=100,unique=True)
	phone=models.CharField(max_length=10,default='')
	USERNAME_FIELD  = 'email'
	REQUIRED_FIELDS =['username']
	def __str__(self):
	    return self.email