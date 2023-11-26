from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

# class CustomUser(AbstractUser):
#     # Dodaj dodatkowe pola, które chcesz przechowywać w modelu użytkownika
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     birth_date = models.DateField(blank=True, null=True)
#     # Inne pola

#     def __str__(self):
#         return self.username
    
# class Image(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Dodaj import User
#     image = models.ImageField(upload_to='images/')

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
