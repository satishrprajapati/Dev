from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=11)

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=100,blank=True,)
    email = models.CharField(max_length=100,blank=True,)
    date_of_birth= models.DateField(blank=True,) 
    picture = models.ImageField(blank=True,)
    department = models.ForeignKey(
        Department, related_name="exployee", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.employee_name


