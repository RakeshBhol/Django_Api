
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Company_App.views import (OrganizationViewSet, DepartmentViewSet, DesignationViewSet,
 EmployeeViewSet, EmployeesAttendanceCollectionViewSet)
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'designation', DesignationViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'employeeattendance', EmployeesAttendanceCollectionViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
]
