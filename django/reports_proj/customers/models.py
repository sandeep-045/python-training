from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=120)
    logo=models.ImageField(default='nopicture.png',upload_to='customers')

    def __str__(self):
        return self.name