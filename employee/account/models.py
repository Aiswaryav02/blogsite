from django.db import models

# Create your models here.
class Regmodel(models.Model):
    empid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    email=models.EmailField()
    eperience=models.IntegerField()
    
    def __str__(self):
       return self.name
   
class Department(models.Model):
    department_name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    office_number=models.IntegerField()

class Manager(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    pic=models.ImageField(upload_to="profilepic",null=True)
