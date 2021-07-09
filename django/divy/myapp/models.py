from django.db import models
from django.utils import timezone
import uuid
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=10)
    created=models.DateTimeField(default=timezone.now)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False  )
    
    def __str__(self):
        return self.name

class Project(models.Model):

    title=models.CharField(max_length=100,null=True)
    description=models.TextField()
    source_link=models.CharField(max_length=100)
    vote_total=models.IntegerField(default=0)
    vote_ratio=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField(Tag)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    options=(('up','up'),('down','down'))
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField()
    value=models.CharField(max_length=20,choices=options)
    created=models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField(Tag)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value