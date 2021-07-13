from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func

# Method-1
# def allowed_users(view_func):

#     def wrapper_func(request,*args,**kwargs):
#         if request.user.is_superuser:
#             return view_func(request,*args,**kwargs)
#         else:
#             return HttpResponse('You are not authorized to view this page')
#     return wrapper_func

def allowed_users(allowed=[]):
    def decorator(view_func):

        def wrapper_func(request,*args,**kwargs):
            
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                print(group,allowed)
            if group in allowed:    
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorized')
        return wrapper_func
    return decorator


def admin_only(view_func):

    def wrapper_func(request,*args,**kwargs):
            
        group=None
        
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
            print(group)
        
        if group=='admins':
            return view_func(request,*args,**kwargs)

        elif group=='customers':
            return redirect('user')
        
    return wrapper_func

