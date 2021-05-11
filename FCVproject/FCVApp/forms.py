from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields='__all__'


        # def clean(self):
        #     total_data=super().clean()
        #     name=total_data['name']
        #     if len(name)<=3:
        #         raise forms.ValidationError('Enter any Charecters')
