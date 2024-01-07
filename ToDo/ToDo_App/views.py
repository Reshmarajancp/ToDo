from django.shortcuts import render,redirect
from django.views.generic import View
from ToDo_App.forms import Register_form,login_form,Task_form
from ToDo_App.models import Task_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.


#DECORATOR
#----------

def signinrequired(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"please login")
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def mylogin(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Task_model.objects.get(id=id)
        if obj.user!= request.user:
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class Register_view(View):
    def get(self,request,*args,**kwargs):
        form=Register_form()
        return render(request,"Reg.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Register_form(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print(form.cleaned_data)
            return redirect('login')
        form=Register_form()
        return render(request,"Reg.html",{"form":form})


class login_view(View):
    def get(self,request,*args,**kwargs):
        form=login_form()
        return render(request,"Login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=login_form(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                print("valid user")
                print(form.cleaned_data)
                login(request,user_obj)
                return redirect('index')
            else:
                print("invalid user")
                messages.error(request,"You should Register first")
            return render(request,"Login.html",{"form":form})
        
class logout_view(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('login')
    
@method_decorator(signinrequired,name="dispatch")    
class TaskView(View):
    def get(self,request,*args,**kwargs):
        form=Task_form()
        data=Task_model.objects.filter(user=request.user).order_by('complete')
        return render(request,"index.html",{"form":form,"data":data})
    def post(self,request,*args,**kwargs):
        form=Task_form(request.POST)
        if form.is_valid():
            print(request.user)
            form.instance.user=request.user
            data=Task_model.objects.filter(user=request.user).order_by('complete')
            form.save()      
            form=Task_form() 
                               
        return render(request,"index.html",{"form":form,"data":data})


@method_decorator(signinrequired,name="dispatch")
@method_decorator(mylogin,name="dispatch")
class Task_update(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task_model.objects.get(id=id)
        if qs.complete == False:
            qs.complete = True
            qs.save()
        elif qs.complete == True:
            qs.complete = False
            qs.save()
        # qs.update(complete=True)
        return redirect("index")
    

@method_decorator(signinrequired,name="dispatch")
@method_decorator(mylogin,name="dispatch")
class Task_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task_model.objects.filter(id=id).delete()
        return redirect("index")
    
class user_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        User.objects.filter(id=id).delete()
        return redirect("reg")