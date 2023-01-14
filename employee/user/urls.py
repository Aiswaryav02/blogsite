from django.urls import path
from .views import*
urlpatterns = [
    path('hme/',Home.as_view(),name="hme"),
    path('profile/',ViewProfile.as_view(),name="profile"),
    path('addbio/',UserProView.as_view(),name="addbio"),
    path('chpsw/',PasswordReset.as_view(),name="chpsw"),
    path('updbio/<int:user_id>',UpdateBioView.as_view(),name="updatebio"),
    path('addcmnt/<int:id>',add_comment,name="addcmnt"),
    path('like/<int:bid>',add_like,name="like"),
    path('myblog/',Myblog.as_view(),name="myblog"),
]

