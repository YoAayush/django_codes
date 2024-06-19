from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Project(models.Model):    
    projectName = models.CharField(max_length=50)
    
class Department(models.Model):
    departmentName = models.CharField(max_length=50)
    projects = models.ManyToManyField(Project)
    
class Employee(models.Model):
    empName = models.CharField(max_length=50)
    age = models.PositiveBigIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    desgination = models.TextField()
    qualification = models.TextField()
    dateOfJoining = models.DateField()
    
    def Clean(self):
        if self.age < 20:
            raise ValidationError("Age should be greater than 20")
        
    def __str__(self):
        return f'{self.empName} - {self.department}'
    
class FileImage(models.Model):
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')