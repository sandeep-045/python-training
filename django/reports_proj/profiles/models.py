from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(default='Some Bio')
    avatar=models.ImageField(default='nopicture.png',upload_to='avatars')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):

        return f'{self.user.username} Profile'