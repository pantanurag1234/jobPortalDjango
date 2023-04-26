from django.contrib import admin
from django.urls import path

#by me
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.empty,name='empty'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('landing/', views.landing, name='landing'),
    path('apply/', views.apply, name='apply')
]
