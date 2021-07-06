from django.db import models

# Create your models here.
class Task(models.Model):

    head=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    lastmodified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.head
    