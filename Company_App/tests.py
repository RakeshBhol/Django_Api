from django.test import TestCase, Client
from .models import Organization, Department
from .serializers import DepartmentSerializer
from rest_framework.decorators import api_view
from django.urls import reverse
from rest_framework.response import Response

class OrganizationTest(TestCase):
    """ Test module for Organization model """

    def setUp(self):
        Organization.objects.create(
            name='Varadhi',address='Bangalore', email='varadhi@gmail.com', phone_no=9875544561)
        Organization.objects.create(
            name='TCS',address='Bangalore', email='tcs@gmail.com', phone_no=2323556461)

    def test_Organization(self):
        Organization_Varadhi = Organization.objects.get(name='Varadhi')
        Organization_TCS = Organization.objects.get(name='TCS')
        self.assertEqual(
            Organization_Varadhi.get_name(), "Varadhi belongs from Bangalore location.")
        self.assertEqual(
            Organization_TCS.get_name(), "TCS belongs from Bangalore location.")






class GetAllDepartmentTest(TestCase):
    """ Test module for GET all Department API """

    def setUp(self):
        Department.objects.create(
            name='Casper', no_of_employee=3)
        Department.objects.create(
            name='Muffin', no_of_employee=1)
        Department.objects.create(
            name='Rambo', no_of_employee=2)
        Department.objects.create(
            name='Ricky', no_of_employee=6)

    def test_get_all_department(self):
        # get API response
        response = Client.get(reverse('get_post_department'))
        # get data from db
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)