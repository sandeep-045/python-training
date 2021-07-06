from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            uname=request.POST.get('username')
            messages.success(request,f'Registration Successful {uname}')
            return redirect('/')
        else:
            return redirect("/signin")
    else:
        form=UserCreationForm()
        context={'form':form}
        return render(request,'users/signin.html',context)
    