from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import Regform,Depform,ManagerForm
from django.contrib import messages
from .models import Regmodel,Department,Manager
# Create your views here.
 
class Reg(View):
    def get(self,request):
        form=Regform()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        form_data=Regform(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            name=form_data.cleaned_data.get('name')
            age=form_data.cleaned_data.get('age')
            em=form_data.cleaned_data.get('email')
            ex=form_data.cleaned_data.get('experience')
            Regmodel.objects.create(name=name,age=age,email=em,eperience=ex)
            messages.success(request,"Registration Completed Successfully")
            return redirect('reg')
        else:
            messages.error(request,"Registration Failed")
            return render(request,"reg.html",{"form":form_data})
class Home(View):
    def get(self,request):
        return render(request,"home.html")
class Viewemp(View):
    def get(self,request):
        emp=Regmodel.objects.all()
        return render(request,"viewemp.html",{'data':emp})
class Deletemp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        eob=Regmodel.objects.get(empid=id)
        eob.delete()
        return redirect('vemp')
class EditEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=Regmodel.objects.get(empid=id)
        form=Regform(initial={'name':emp.name,'age':emp.age,'email':emp.email,'experience':emp.eperience})
        return render(request,"editemp.html",{'form':form})
    def post(self,request,*args,**kwargs):
        form=Regform(request.POST)
        id=kwargs.get("id")
        if form.is_valid():
            name=form.cleaned_data.get('name')
            age=form.cleaned_data.get('age')
            em=form.cleaned_data.get('email')
            ex=form.cleaned_data.get('experience')
            Regmodel.objects.filter(empid=id).update(name=name,age=age,email=em,eperience=ex)
            return redirect('vemp')
        else:
            return redirect('editemp')
class DeptView(View):
        def get(self,request,*args,**kwargs):
            form=Depform()
            return render(request,"deptreg.html",{'form':form})
        def post(self,request,*args,**kwargs):
            form_data=Depform(request.POST)
            if form_data.is_valid():
                form_data.save()
                messages.success(request,"department added")
                return redirect('h')
            else:
                messages.error(request,"department adding failed")
                return redirect('dept')
class Viewdept(View):
    def get(self,request):
        dept=Department.objects.all()
        return render(request,"viewdept.html",{'data':dept})
class Deletedept(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        dept=Department.objects.get(id=did)
        dept.delete()
        return redirect('vdpt')
class DeptEdit(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        dept=Department.objects.get(id=d_id)
        form=Depform(instance=dept)
        return render(request,"editdept.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        dept=Department.objects.get(id=d_id)
        form_data=Depform(request.POST,instance=dept)
        if form_data.is_valid():
            form_data.save()
            return redirect('vdpt')
        else:
            return redirect('editdept')
        
class ManagerReg(View):
    def get(self,req):
        form=ManagerForm()
        return render(req,"addmanager.html",{'form':form})
    def post(self,req):
        form_data=ManagerForm(req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('h')
        else:
            return redirect('addman')
class ViewManager(View):
    def get(self,request):
        data=Manager.objects.all()
        return render(request,"manageview.html",{'data':data})
class Deleteman(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        mng=Manager.objects.get(id=did)
        mng.delete()
        return redirect('viewman')
class EditMan(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        mng=Manager.objects.get(id=d_id)
        form=ManagerForm(instance=mng)
        return render(request,"editmanager.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        mng=Manager.objects.get(id=d_id)
        form_data=ManagerForm(request.POST,files=request.FILES,instance=mng)
        if form_data.is_valid():
            form_data.save()
            return redirect('viewman')
        else:
            return redirect('addman') 
class Index(View):
    def get(self,request):
        return render(request,"index.html")