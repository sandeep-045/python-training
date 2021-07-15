from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if not request.user.is_authenticated:
        error_message=None
        form=AuthenticationForm()
        if request.method=='POST':
            form=AuthenticationForm(data=request.POST)
            if form.is_valid:
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)

                if user is not None:
                    login(request,user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect('sales:home')
            else:
                error_message='Something went wrong'
        
        context={
            'form':form,
            'error_message':error_message
        }
        
        return render(request,'auth/login.html',context)
    else:
        return HttpResponse('You are already logged in')

@login_required()
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'auth/logout.html')
    return render(request,'auth/logout.html')