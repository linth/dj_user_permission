'''
# extending the existing user model.
https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#extending-user

# custom auth 
https://docs.djangoproject.com/en/5.0/topics/auth/customizing/
'''
from typing import Any
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from extend_user.models import Employee
from extend_user.serializers import EmployeeSerializer

import logging

logger = logging.getLogger('my-logging')


class EmployeeList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    serializer_class = Employee
    permission_classes = [IsAuthenticated]

    def get(self, request):
        self.queryset = Employee.objects.all()
        if (self.queryset.exists()):
            logger.debug('queryset is empty.')
            return Response([], status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(self.queryset, many=True)
        content = {
            'user': str(request.user), # django.contrib.auth.User instance.
            'auth': str(request.auth), # None
        }
        
        return Response(serializer.data, status=status.HTTP_200_OK)

