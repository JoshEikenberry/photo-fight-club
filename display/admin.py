from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Photos, Users, Categories

admin.site.register(Photos)
admin.site.register(Users)
admin.site.register(Categories)
