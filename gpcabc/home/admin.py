from django.contrib import admin
from home.models import Contact, Registration, Story, Registered
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Registration)
@admin.register(Story)
@admin.register(Contact)
@admin.register(Registered)

class RegisteredAdmin(ImportExportModelAdmin):
    pass

