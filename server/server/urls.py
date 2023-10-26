# urls.py

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('login/',views.index,name='login')
]
