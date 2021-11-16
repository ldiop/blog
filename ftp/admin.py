# Register your models here.
from django.contrib import admin
from .models.models import T_user

class T_userAdmin(admin.ModelAdmin):
    fields = ['ftpUsername', 'ftpPassword', 'ftpHomeDir', 'nom', 'societe', 'dateExpiration', 'email', 'telephone', 'contact_interne', 'filewatch_contact' ]
# Register your models here.
admin.site.register(T_user)

