"""
URL configuration for asistencias project.

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
from asistencia import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/',login_required(views.index), name='index'),
    path('index2/',login_required(views.index2), name='index2'),
    path('ap_personal/',login_required(views.ap_personal), name='personal'),
    path('', admin.site.urls),
]
