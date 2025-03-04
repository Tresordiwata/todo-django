from django.contrib import admin
from .models import User,PostUser

# Register your models here.

admin.site.register([PostUser,User])
