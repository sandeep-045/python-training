from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='loginuser')
def my_profile_view(request):
    user=Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None,request.FILES or None,instance=user)
    confirm=False  
    if form.is_valid():
        confirm=True
        form.save()
    context={'prof':user,'form':form,'confirm':confirm}
    return render(request,'profiles/main.html',context)