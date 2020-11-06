from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView 
from .models import Employee, Department
from .forms import EmployeeForm



class EmployeeList(ListView): 
    model = Employee
    template_name = 'staff/employee_list.html'

class EmployeeDetail(DetailView): 
    model = Employee
    template_name = 'staff/employee_details.html'

class DepartmentList(ListView): 
    model = Department
    template_name = 'staff/department_list.html'

class EmployeeCreate(CreateView): 
    form_class = EmployeeForm
    template_name = 'staff/employee_create.html'
    success_url = 'employee_list'    

class DepartmentDetail(ListView): 
    model = Employee
    template_name = 'staff/department_details.html'  
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['obj_list'] = Employee.objects.filter(department_id=self.kwargs['pk'])
        return context



