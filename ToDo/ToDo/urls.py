"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ToDo_App.views import Register_view,login_view,logout_view,TaskView,Task_update,Task_delete,user_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',Register_view.as_view(),name='reg'),
    path('',login_view.as_view(),name='login'),
    path('logout/',logout_view.as_view(),name='logout'),
    path('index/',TaskView.as_view(),name='index'),
    path('index/edit/<int:pk>',Task_update.as_view(),name='edit'),
    path('index/remove/<int:pk>',Task_delete.as_view(),name='dlt'),
    path('usredlt/<int:pk>/',user_delete.as_view(),name='userdlt'),

]
