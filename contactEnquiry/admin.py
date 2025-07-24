from django.contrib import admin
from contactEnquiry.models import contactEnquiry

# Register your models here.


class contactenquiry(admin.ModelAdmin):
    list_display=('name','email','phone')
admin.site.register(contactEnquiry,contactenquiry)  
# service it is a model name , serviceAdminn is a class name

