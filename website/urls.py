"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Event_Management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events'),
    path('contact/',views.contact,name='contact'),
    path('booking/',views.booking,name='booking'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('wedding/', views.wedding,name='wedding'),
    path('eng/', views.eng,name='eng'),
    path('rece/', views.rece,name='rece'),
    path('bir/', views.bir,name='bir'),
    path('par/', views.par,name='par'),
    path('get/', views.get,name='get'),
]
