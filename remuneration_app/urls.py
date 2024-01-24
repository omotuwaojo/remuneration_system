from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employee/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
]
    #path('employees/', views.employee_list, name='employee_list'),
    # Other URLs for additional functionalities or pages
