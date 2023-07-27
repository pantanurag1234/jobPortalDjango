from django.contrib import admin
from django.urls import path

#by me
from . import views
from django.urls import include

app_name = 'JobPortalDjango'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.empty,name='empty'),
    path('login/', views.custom_login_view, name='custom_login_view'),
    path('register/', views.custom_register_view, name='custom_register_view'),
    path('landing/', views.landing, name='landing'),
    path('apply/', views.apply, name='apply'),
    # path('', include("django.contrib.auth.urls"))
    path('logout/', views.custom_logout_view, name='logout')
]
