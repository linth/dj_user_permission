from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from faker import Faker

import logging

logger = logging.getLogger('my-logging')


@api_view(['GET'])
def gen_faker_user(request, num: int = 100):
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
    