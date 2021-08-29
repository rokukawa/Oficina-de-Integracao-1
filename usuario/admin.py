from django.contrib import admin
from .models import *
from django.contrib.auth import admin as auth_admin

# Register your models here.

#não está sendo usada a classe listandoUsuario
class listandoUsuario(admin.ModelAdmin):
    list_display = ('email', 'username')
    list_display_links = ('email', 'username')
    search_fields = ('email',)
    list_per_page = 10

admin.site.register(Usuario, auth_admin.UserAdmin)
