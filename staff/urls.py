


from django.contrib import admin
from django.urls import path
from . import views
app_name = 'company_staff'

urlpatterns = [
    path('employee', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee_view/<int:pk>', views.EmployeeDetail.as_view(), name='employee_view'),
    path('department_details/<int:pk>', views.DepartmentDetail.as_view(), name='department_details'),
    path('employee_list', views.EmployeeList.as_view(), name='employee_list'),
    path('department_list', views.DepartmentList.as_view(), name='dept_list'),

]