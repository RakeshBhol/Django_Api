from django.shortcuts import render
from Company_App.models import *
from Company_App.serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class OrganizationViewSet(viewsets.ModelViewSet):
    #A simple ViewSet for viewing and editing accounts.
    queryset = Organization.objects.all().order_by('id')
    serializer_class = OrganizationSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class DepartmentViewSet(viewsets.ModelViewSet):
    #A simple ViewSet for viewing and editing accounts.
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class DesignationViewSet(viewsets.ModelViewSet):
    #A simple ViewSet for viewing and editing accounts.
    queryset = Designation.objects.all().order_by('id')
    serializer_class = DesignationSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class EmployeeViewSet(viewsets.ModelViewSet):
    #A simple ViewSet for viewing and editing accounts.
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class EmployeesAttendanceCollectionViewSet(viewsets.ModelViewSet):
    #A simple ViewSet for viewing and editing accounts.
    queryset = EmployeesAttendanceCollection.objects.all().order_by('id')
    serializer_class = EmployeesAttendanceCollectionSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def get_post_department(request):
    # get all Department
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)
    # insert a new record for a Department
    elif request.method == 'POST':
        return Response({})