from django.contrib import admin
from .models import Employee,Department,Project,FileImage

# Register your models here.
class customize(admin.ModelAdmin):
    list_display = ['empName','age','qualification','dateOfJoining']
    
admin.site.register(Employee,customize)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(FileImage)