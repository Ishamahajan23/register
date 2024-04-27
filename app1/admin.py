from django.contrib import admin
# from django.contrib.admin.sites import site
from app1.models import Join_users
from app1.models import contact

# Register your models here.

class JoinAdmin(admin.ModelAdmin):
 list_display=('username','email','age','location','interests','schedule','frequency','types')

admin.site.register(Join_users,JoinAdmin)

class contactAdmin(admin.ModelAdmin):
 list_display=('email','mobilenumber','message')

admin.site.register(contact,contactAdmin)

