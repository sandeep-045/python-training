from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    context={'blogs':Post.objects.all()}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html',{'title':'about'})