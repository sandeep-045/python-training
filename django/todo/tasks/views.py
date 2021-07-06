from django.shortcuts import render,HttpResponse,redirect   
from tasks.models import *
import datetime

def home(request):
    if request.method=="POST":
        title=request.POST.get("title")
        status=request.POST.get("status")
        if status=="on":
            status=True
        else:
            status=False   
        t=Task(head=title,status=status,lastmodified=datetime.datetime.now())
        if title=="":
            return  redirect("/")
        t.save()
        return redirect('/')
    tasks=Task.objects.all()
    content={'tasks':tasks}
    return render(request,'list.html',content)

def update_task(request,pk):
        task=Task.objects.get(id=pk)
        t={'task':task}
        if request.method=='POST':
            title=request.POST.get('head')
            task.head=title
            task.lastmodified=datetime.datetime.now()
            task.save()
            return redirect("/")
        return render(request,'update.html',t)

def delete_task(request,pk):
    Task.objects.get(id=pk).delete()
    return redirect("/")

# Create your views here.
