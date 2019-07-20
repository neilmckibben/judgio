"""judgio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from adminplus.sites import AdminSitePlus

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.views.generic.base import TemplateView
from judging import views 
=======

from judging import views
>>>>>>> 4931462f491fcff27b00099c66413d2154266d25

# use adminplus app
admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    # login endpoint
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', views.register),
=======
    path('', views.home, name='home'),
>>>>>>> 4931462f491fcff27b00099c66413d2154266d25
]

urlpatterns += staticfiles_urlpatterns()
