from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required, user_passes_test
from .form import EmployeeForm
#import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create a group (e.g., HR) and assign permissions
hr_group, created = Group.objects.get_or_create(name='HR')
hr_group.permissions.add(Permission.objects.get(codename='add_employee'))
#hr_group.permissions.view(Permission.objects.get(codename='view_employee'))

# Assign more permissions as needed

# Assign users to groups
# user.groups.add(hr_group)

@login_required
@user_passes_test(lambda user: user.groups.filter(name='HR').exists(), login_url='/login/') 
def add_employee(request):
    # Your view logic for adding employees
    # ...
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to employee list view
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})



def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    # Calculate bonus based on performance score
    performance_score = employee.performance_score
    if performance_score == 5:
        bonus_percentage = 0.10
    elif performance_score == 4:
        bonus_percentage = 0.05
    elif performance_score == 3:
        bonus_percentage = 0.02
    else:
        bonus_percentage = 50

    bonus = bonus_percentage * employee.salary

    return render(request, 'employee_detail.html',
                   {'employee': employee, 'bonus': bonus})

# remuneration_app/edit_employee

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to employee list view
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee_id': employee_id})

# remuneration_app/delete_employee

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  # Redirect to employee list view after deletion
    return render(request, 'confirm_delete.html', {'employee': employee})

#Filtering Employees
def employee_list(request):
    employees = Employee.objects.all()

    # Filtering based on query parameters
    name_query = request.GET.get('name')
    if name_query:
        employees = employees.filter(name__icontains=name_query)

    # Add more filtering options as needed (salary, performance_score, etc.)

    return render(request, 'employee_list.html', {'employees': employees})

#To enable sorting, modify the view to handle sorting based on specific criteria (e.g., salary, performance score):

def employee_list(request):
    employees = Employee.objects.all()

    # Sorting based on query parameters
    sort_by = request.GET.get('sort')
    if sort_by == 'salary':
        employees = employees.order_by('salary')
    elif sort_by == 'performance':
        employees = employees.order_by('-performance_score')

    return render(request, 'employee_list.html', {'employees': employees})

def analytics_dashboard(request):
    # Query the database to get average salaries per department
    # Example query: 
    # average_salaries = Employee.objects.values('department').annotate(avg_salary=Avg('salary'))
    
    # Dummy data for demonstration
    departments = ['IT', 'HR', 'Finance', 'Sales']
    average_salaries = [60000, 55000, 62000, 58000]  # Replace with actual data
    
    # Create a bar chart using Matplotlib
   # plt.figure(figsize=(8, 6))
   # plt.bar(departments, average_salaries)
   # plt.xlabel('Department')
   # plt.ylabel('Average Salary')
   # plt.title('Average Salaries per Department')
   # plt.xticks(rotation=45)
   # plt.tight_layout()

    # Save the plot to a file or memory buffer
   # plt.savefig('media/analytics/average_salaries.png')  # Save to a file
    # OR
    # from io import BytesIO
    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # return buffer

    return render(request, 'analytics_dashboard.html')


