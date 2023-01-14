from django import forms
from .models import Department,Manager
class Regform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Your Name","class":"form-control"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Your Age","class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter Your email id","class":"form-control"}))
    experience=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Your Experience","class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        ex=cleaned_data.get('experience')
        if ex<0:
            msg="invalid experience"
            self.add_error('experience',msg)
# class Depform(forms.Form):
    # dept_name=forms.CharField(label="Department Name")
    # description=forms.CharField(label="Description")
    # office_no=forms.IntegerField(label="office number")
class Depform(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"
        widgets={
            'department_name':forms.TextInput(attrs={'placeholder':'Enter Deparment Name','class':'form-control'}),
            'description':forms.TextInput(attrs={'placeholder':'Enter Description','class':'form-control'}),
            'office_number':forms.TextInput(attrs={'placeholder':'Enter Deparment Room No','class':'form-control'})
        }
class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields="__all__"
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'pic':forms.FileInput(attrs={'class':'form-control'})
     
        }        
