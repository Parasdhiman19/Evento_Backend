from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# the useradmin help us to dispaly users data on admin pannel with more depth 
admin.site.register(User, UserAdmin)