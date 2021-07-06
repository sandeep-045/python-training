from django.shortcuts import render,HttpResponse
from myapp import forms
from myapp import models
# Create your views here.

def home(request):
	if request.method=="POST":
		form=forms.UserForm(request.POST)
		form.save()
	form=forms.UserForm()
	content={'form':form}
	return render(request,'home.html',content)
def show(request,id):
	print()

	return HttpResponse(f"Hello {models.User.objects.get(id=1).name}")
