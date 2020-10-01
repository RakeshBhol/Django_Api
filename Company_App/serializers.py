from rest_framework import serializers
from Company_App.models import *


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'address', 'email', 'phone_no']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'no_of_employee']


class DesignationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'title']


class EmployeesAttendanceCollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeesAttendanceCollection
        fields = ['id', 'start_time', 'end_time', 'break_start', 'break_end']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeesAttendanceCollectionSerializer(read_only=True, many=True)
    class Meta:
        model = Employee
        fields = ['id', 'e_name', 'e_id', 'salary', 'e_phone_no', 'employee']



