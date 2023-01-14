from django.urls import path
# from .views import Reg,Viewemp,Deletemp,EditEmp,DeptView,Viewdept,Deletedept,DeptEdit
from .views import *

urlpatterns = [
    path('reg/',Reg.as_view(),name="reg"),
    path('view/',Viewemp.as_view(),name="vemp"),
    path('del/<int:id>',Deletemp.as_view(),name="delemp"),
    path('edit/<int:id>',EditEmp.as_view(),name="editemp"),
    path('dept',DeptView.as_view(),name="dept"),
    path('viewdpt/',Viewdept.as_view(),name="vdpt"),
    path('deldept/<int:did>',Deletedept.as_view(),name="deledept"),
    path('deptedit/<int:did>',DeptEdit.as_view(),name="editdept"),
    path('addman/',ManagerReg.as_view(),name="addman"),
    path('viewman/',ViewManager.as_view(),name="viewman"),
    path('delman/<int:did>',Deleteman.as_view(),name="delman"),
    path('aditman/<int:did>',EditMan.as_view(),name="editman"),
    path('index/',Index.as_view()),
]
