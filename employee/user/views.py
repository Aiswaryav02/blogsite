from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.models import UserProfile
from .forms import UseProForm,PassForm,BlogForm,CommentForm
from .models import BlogModel,CommentModel
from django.contrib.auth import authenticate
# Create your views here.
# decorators
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,*kwargs)
        else:
            return redirect('log')
    return wrapper

@method_decorator(signin_required,name="dispatch")
class Home(CreateView):
    # def get(self,req,*args,**kwargs):
    #     user=req.user
    #     return render(req,"home2.html",{'user_data':user})
    template_name="home2.html"
    model=BlogModel
    form_class=BlogForm
    success_url=reverse_lazy('hme')
    def form_valid(self, form) :
        form.instance.author=self.request.user
        self.object=form.save()
        messages.success(self.request,"Blog Added Successfully")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog=self.model.objects.all().order_by('-date')
        context['blog']=blog
        cmnt=CommentForm()
        context['comment']=cmnt
        context['comments']=CommentModel.objects.all()
        return context
def add_comment(request,*args,**kwargs):
        print("hi")
        if request.method=='POST':
            cmnt=request.POST.get('comment')
            user=request.user
            b_id=kwargs.get('id')
            blog=BlogModel.objects.get(id=b_id)
            CommentModel.objects.create(comment=cmnt,user=user,blog=blog)
            messages.success(request,"comment added")
            return redirect('hme')
def add_like(request,*args,**kwargs):
    blog_id=kwargs.get('bid')
    user=request.user
    blog=BlogModel.objects.get(id=blog_id)
    blog.liked_by.add(user)
    blog.save()
    return redirect('hme')

@method_decorator(signin_required,name="dispatch")
class ViewProfile(TemplateView):
    # def get(self,req,*args,**kwargs):
    #         user=req.user
    #         return render(req,"profile.html",{'user_data':user})
    template_name="profile.html"

class UserProView(CreateView):
    model=UserProfile
    form_class=UseProForm
    template_name='bio.html'
    success_url=reverse_lazy('profile')
        # def post(self, request, *args, **kwargs):
        #     form_data=self.form_class(request.POST,request.FILES)
        #     if form_data.is_valid():
        #         form_data.instance.user=request.user
        #         form_data.save()
        #         return redirect('profile')
        #     else:
        #         return redirect('addbio')
    def form_valid(self, form) :
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Bio Added Successfully")
        return super().form_valid(form)
        
class PasswordReset(FormView):
    template_name="resetpass.html"
    form_class=PassForm

    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            old=form_data.cleaned_data.get('old_password')
            new=form_data.cleaned_data.get('new_password')
            cp=form_data.cleaned_data.get('confirm_password')
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==cp:
                    user.set_password(cp)
                    user.save()
                    messages.success(request,"password changed!!")
                    return redirect('log')
                else:
                    messages.error(request,"new password and confirm password mismatches!!")
                    return redirect('chpsw')
            else:
                messages.error(request,"old password mismatches!!")
                return redirect('chpsw')
        else:
            messages.error(request,form_data.errors)
            return redirect('chpsw')
class UpdateBioView(UpdateView):
    template_name='updatebio.html'
    form_class=UseProForm
    model=UserProfile
    success_url=reverse_lazy('profile')
    pk_url_kwarg='user_id'
    def form_valid(self, form) :
        self.object=form.save()
        messages.success(self.request,"Bio Updated")
        return super().form_valid(form)
    # def get(self,req,*args,**kwargs):
    #     id=kwargs.get('user_id')
    #     userpro=UserProfile.objects.get(user=id)
    #     print(userpro)
    #     return HttpResponse(userpro.gender)
class Myblog(TemplateView):
        template_name="myblogs.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            blog=BlogModel.objects.filter(author=self.request.user)
            context['data']=blog
            context['cmnts']=CommentModel.objects.all()
            return context