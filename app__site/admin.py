from django.contrib import admin
from .models import Form

# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'last_name', 'email', 'occupation']
    search_fields= ['first_name', 'last_name', 'email', 'occupation']
    
    model = Form
    extra_field = 1
    
    
admin.site.register(Form, FormAdmin )