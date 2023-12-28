from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.serializers import serialize

from faker import Faker

import logging
from extend_user.models import Employee

from extend_user.serializers import EmployeeSerializer
from users.serializers import UserSerializer

logger = logging.getLogger('my-logging')


@api_view(['GET'])
def gen_faker_user(request, num: int = 100):
    # create fake user.
    logger.debug('call gen_faker_user.')
    logger.debug(f'number: {num}')

    if request.method == 'GET':
        fake = Faker()
        try:
            for _ in range(num):
                name = fake.name().split(' ')
                User.objects.create_user(username=name[0].join(name[1]),
                                        password='admin',
                                        email=name[0] + '@gmail.com',
                                        first_name=name[0],
                                        last_name=name[1],)
        except Exception as e:
            logger.debug(f'error: {e}')
    message = 'generate ' + str(num) + ' users.'
    return Response({'message': message }, 
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def gen_faker_extend_user(request, num: int = 20):
    # create fake employee.
    logger.debug('call gen_faker_extend_user')
    logger.debug(f'number: {num}')
    
    if request.method == 'GET':
        logger.debug('request method get.')
        fake = Faker()
        user = User.objects.filter(id__lte=20)
        logger.debug(f'user: {user.get(id=1)}')
        logger.debug(f'exists: {user.get(id=1)}')
        user_serializer = UserSerializer(user, many=True)
        employee = Employee()
        try:
            for i in range(num):
                if user.get(id=i):
                    r = user.get(id=i)
                    logger.debug('user ID: {r}')
                    employee(user=user, department='Google')
                    # e.save()
            e = Employee.objects.all()
            es = EmployeeSerializer(e, many=True)
            return Response({'user': es.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error('generate employee data failure.')
            logger.error(f'error: {e}')
            return Response({'message': 'something wrong.'}, status=status.HTTP_404_NOT_FOUND)