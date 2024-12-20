from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("ppt/",views.PPT,name="ppt"),
    path("StudyMaterial/",views.Study,name="StudyMaterial"),
    path("Modules/",views.Module,name="Modules"),
    path("Practicals/",views.Practicals,name="Modules"),
    path("trial/",views.trail,name="Test"),
    path("PYQS/",views.PYQ,name="PYQ"),
    path('adminpanel/',views.admin,name='admin'),
    path('update/<int:id>/',views.update,name="Update"),
    path('delete/<int:id>/',views.delete_file,name="Delete"),
    path("create/",views.create_file,name="Create"),
    path("logout/",views.logout_user,name="logout"),
    path("login/",views.login_user,name="login"),
    path('download/<int:id>/',views.download_file, name='download_file'),
]