from django.contrib import admin
from . models import *

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'email', 'phone_no']

admin.site.register(Organization, OrganizationAdmin)



class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name', 'no_of_employee']

admin.site.register(Department, DepartmentAdmin)



class DesignationAdmin(admin.ModelAdmin):
    fields = ['title']

admin.site.register(Designation, DesignationAdmin)




class EmployeeAdmin(admin.ModelAdmin):
    fields = ['e_name', 'e_id', 'salary', 'e_phone_no']

admin.site.register(Employee, EmployeeAdmin)




class EmployeesAttendanceCollectionAdmin(admin.ModelAdmin):
    fields = ['employee', 'start_time', 'end_time', 'break_start', 'break_end']

admin.site.register(EmployeesAttendanceCollection, EmployeesAttendanceCollectionAdmin)