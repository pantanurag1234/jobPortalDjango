from django.contrib import admin

# Register your models here.

from .models import organisations
admin.site.register(organisations)

from .models import registration
admin.site.register(registration)