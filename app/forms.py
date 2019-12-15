from django import forms
from . models import *

class VehicleForm(forms.ModelForm):
    

    class Meta:
        model=Vehicle
        fields='__all__'  
        