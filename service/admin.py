from django.contrib import admin
from service.models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_dec')


admin.site.register(Service,ServiceAdmin)  
# service it is a model name , serviceAdminn is a class name