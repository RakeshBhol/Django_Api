from django.db import models
from django.core.exceptions import ValidationError 
  
# creating a email validator function 
def validate_email(value): 
    if "@" and "." in value: 
        return value 
    else: 
        raise ValidationError("Please enter valid email format")


# creating a phone validator function 
def validate_phone(value): 
    if len(str(value)) == 10: 
        return value 
    else: 
        raise ValidationError("Please enter 10 digit mobile number only")


#Organization Model
class Organization(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(null=True)
    email = models.CharField(max_length=30, null=True, validators=[validate_email])
    phone_no = models.PositiveIntegerField(null=True, validators=[validate_phone])

    def get_name(self):
        return self.name + ' belongs from ' + self.address + ' location.'

    def __str__(self):
        return self.name


#Department Model
class Department(models.Model):
    name = models.CharField(max_length=30)
    no_of_employee = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name



#Designation Model
class Designation(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


#Employee Model
class Employee(models.Model):
    e_name = models.CharField(max_length=30)
    e_id = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    e_phone_no = models.IntegerField(null=True, validators=[validate_phone])

    def __str__(self):
        return self.e_name



#Attendance System of Employee
class EmployeesAttendanceCollection(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    break_start = models.DateTimeField()
    break_end = models.DateTimeField()
    

    def __str__(self):
        return "Attendance of {}".format(self.employee.e_name)
