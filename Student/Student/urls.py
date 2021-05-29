"""Student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.Insertrecord),
    path('Insertrecord',views.Insertrecord,name='Insertrecord'),
    path('AdminRegister',views.Registerrecord),
    path('AdminRegister',views.Registerrecord,name='Registerrecord'),
    path('',views.Home),
    path('About',views.About,name='About'),
    path('LoginView',views.LoginView,name='LoginView'),
    path('LoginView1',views.LoginView1,name='LoginView1'),
    path('Contact',views.Contact,name='Contact'),
    path('Edit',views.Edit,name='Edit'),
    path('ViewEditSave',views.ViewEditSave,name='ViewEditSave'),
    path('Logout',views.Logout,name='Logout'),
    path('Delete',views.Delete,name='Delete'),
    path('StudentLoginView',views.StudentView,name='StudentView'),
    



]
