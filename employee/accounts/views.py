from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import send_mail
# Create your views here.


# class Home(View):
#     def get(self,req):
#         return render(req,"home1.html")

class Home(TemplateView):
    template_name='home1.html'
    
# class Signup(View):
#     def get(self,req):
#         form=SignupForm()
#         return render(req,"register.html",{'form':form})
#     def post(self,request):
#         form_data=SignupForm(request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Registered successfully")
#             return redirect('h')
#         else:
#             messages.error(request,"Registration failed")
#             return redirect('reg')
class Signup(CreateView):
    model=User
    form_class=SignupForm
    template_name='register.html'
    success_url=reverse_lazy('h')
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="you are regitered in blogapp.\n you username:"+str(uname)+"\n password:"+str(pwd)
            form_data.save()
            send_mail(
                'BlogApp Registrartion',
                msg,
                'you are successfully registered in blogapp',
                'aishuvivek2002@gmail.com',
                [email_id],
                fail_silently=True
            )
            messages.success(request,"registration completed!!")
            return redirect('h')
        else:
            messages.error(request,"registration failed")
            return render(request,"register.html",{'form':form_data})
# class LoginView(View):
#     def get(self,req):
#         form=LoginForm()
#         return render(req,"login1.html",{'form':form})
#     def post(self,req):
#             un=req.POST.get('username')
#             pw=req.POST.get('password')
#             user=authenticate(req,username=un,password=pw)
#             if user:
#                 login(req,user)
#                 return redirect("hme")
#             else:
#                 return redirect("log")
class LoginView(FormView):
    form_class=LoginForm
    template_name='login1.html'
    def post(self,req):
            un=req.POST.get('username')
            pw=req.POST.get('password')
            user=authenticate(req,username=un,password=pw)
            if user:
                login(req,user)
                return redirect("hme")
            else:
                messages.error(req,"incorrect password")
                return redirect("log")



class SignOut(View):
    def get(self,req,*args,**kwargs):
        logout(req)
        return redirect('log')



