from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):   
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    img=models.ImageField(null=True,blank=True)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CAT=(('Indoor','Indoor'),('Outdoor','Outdoor'))
    name=models.CharField(max_length=20)
    price=models.FloatField(null=True)
    description=models.TextField(max_length=200)
    category=models.CharField(max_length=200,choices=CAT)
    date_created=models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STA=(('Pending','Pending'),('OutForDelivery','OutForDelivery'),('Delivered','Delivered'))
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=200,choices=STA)
    date_created=models.DateTimeField(auto_now_add=True)
    note=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.customer.name.split(' ')[-1]}'s order"