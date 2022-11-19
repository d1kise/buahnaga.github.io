from django import forms  
from crud.models import TableCars

class CarsForm(forms.ModelForm):
    class Meta:  
        model = TableCars
        fields = "__all__"