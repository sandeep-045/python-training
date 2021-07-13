from django.shortcuts import render,redirect
from accounts.forms import *
from accounts.decorators import *
from django.contrib.auth.decorators import login_required
from accounts.models import *
from accounts.forms import *
from accounts.filters import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.forms import inlineformset_factory
# Create your views here.

@unauthenticated_user
def RegisterUser(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            
            messages.success(request,f'Registration successful {request.POST.get("username")}')
            return redirect('login')

    form=UserRegistrationForm()
    context={'form':form}
    return render(request,'accounts/register.html',context)

@unauthenticated_user
def LoginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request,messages.INFO,'Username or Password is Incorrect')
            return render(request,'accounts/login.html')

    return render(request,'accounts/login.html')

@login_required(login_url='login')
def LogoutUser(request):
    logout(request)
    return render(request,'accounts/logout.html')  

    
@login_required(login_url='login')
def ProductList(request):

    products=Product.objects.all() 
    context={'products':products}
    return render(request,'accounts/products.html',context)

@login_required(login_url='login')
@admin_only
def Dashboard(request):

    orders=Order.objects.order_by('-date_created')
    customers=Customer.objects.all()    
    pending=Order.objects.filter(status='Pending').count()
    delivered=Order.objects.filter(status='Delivered').count()
    total=Order.objects.all().count()
    context={'customers':customers,'orders':orders,'pending':pending,'delivered':delivered,'total':total}
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login')
def CustomerDetail(request,pk):
    
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    fil=OrderFilter(request.GET,queryset=orders)
    orders=fil.qs
    context={'customer':customer,'orders':orders,'filter':fil}
    
    return render(request,'accounts/customers.html',context)

@login_required(login_url='login')
@allowed_users(allowed=['customers'])
def UserPage(request):
    orders=request.user.customer.order_set.order_by('-date_created')
    delivered=request.user.customer.order_set.filter(status='Delivered').count()
    total=request.user.customer.order_set.all().count()
    pending=request.user.customer.order_set.filter(status='Pending').count()
    context={'orders':orders,'total':total,'delivered':delivered,'pending':pending}
    return render(request,'accounts/user.html',context)

@login_required(login_url='login')
@allowed_users(allowed=['customers'])
def accountSettings(request):
    ins=Customer.objects.get(user=request.user)
    form=CustomerForm(instance=ins)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=ins)
        form.save()
    context={'form':form}
    return render(request,'accounts/account_settings.html',context)

def CreateOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=1)
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(), instance=customer)
   
    if request.method=="POST":
        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'accounts/createorder.html',context)

def UpdateOrder(request,pk):
    ins=Order.objects.get(id=pk)
    form=OrderForm(request.POST or None,instance=ins)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    context={'form':form}
    return render(request,'accounts/createorder.html',context)

def DeleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    context={'order':order}
    if request.method=='POST':

        order.delete()
        return redirect('/')
    return render(request,'accounts/deleteorder.html',context)