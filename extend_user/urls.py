from django.urls import path, include

from .views import EmployeeList

urlpatterns = [
    path('', view=EmployeeList.as_view(), name='employee-list'),
]