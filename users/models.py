from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    role = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
