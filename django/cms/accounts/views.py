from django.shortcuts import render,redirect
from accounts.models import *
from accounts.forms import *
from django.forms import inlineformset_factory
# Create your views here.

def ProductList(request):

    products=Product.objects.all() 
    context={'products':products}
    return render(request,'accounts/products.html',context)

def Dashboard(request):

    orders=Order.objects.order_by('-date_created')
    customers=Customer.objects.all()    
    pending=Order.objects.filter(status='Pending').count()
    delivered=Order.objects.filter(status='Delivered').count()
    total=Order.objects.all().count()
    context={'customers':customers,'orders':orders,'pending':pending,'delivered':delivered,'total':total}
    return render(request,'accounts/dashboard.html',context)

def CustomerDetail(request,pk):
    
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    context={'customer':customer,'orders':orders}
    
    return render(request,'accounts/customers.html',context)

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