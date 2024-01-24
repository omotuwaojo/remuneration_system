# remuneration_app/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'salary', 'performance_score']  # Add other fields as needed

def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < 0:
            raise forms.ValidationError("Salary should be a positive value.")
        # Add more validation rules if needed
        return salary