from django.contrib import admin


from . models import *
from django.utils.html import format_html
 

class VehicleAdmin(admin.ModelAdmin): 
    list_display= ('vehicle_number', 'vehicle_insurance')

admin.site.register(Vehicle,VehicleAdmin)

