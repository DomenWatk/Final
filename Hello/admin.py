from django.contrib import admin
from Hello.models import Stocksheld
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Stocksheld)




class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)