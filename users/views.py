from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# from users.models import CustomUser
# from users.serializers import CustomUserSerializer
from users.serializers import UserSerializer
from users.permissions import IsOwnerCanRead, IsOwnerOrReadOnly

import logging
# https://testdriven.io/blog/django-custom-user-model/
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-endpoints-for-our-user-models
'''
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "password": "pbkdf2_sha256$720000$MxnRh7D4XVhfLzyc2D0Abw$YJfsJY0Oi9b63/c0+6WpBi+RY9eOpUhhz3GllBo3sEw=",
        "last_login": "2023-12-06T09:30:58.658699Z",
        "is_superuser": true,
        "email": "admin@gmail.cm",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2023-12-06T08:56:29.619743Z",
        "groups": [],
        "user_permissions": []
    }
]

'''
logger = logging.getLogger('my-logging')


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, 
                          IsOwnerCanRead]
    
    def get(self, request, *args, **kwargs):
        self.queryset = User.objects.filter(username=request.user)
        logger.debug('call restful api for user list.')
        return super().get(request, *args, **kwargs)

    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, 
                          IsOwnerCanRead]
    
    def get(self, request, *args, **kwargs):
        logger.debug('call restful api for user detail.')
        return super().get(request, *args, **kwargs)




# class CustomUserList(APIView):
#     serializer_class = CustomUserSerializer

#     def get(self, request, fromat=None):
#         cu = CustomUser.objects.all().filter(is_superuser=False)

#         logger.debug('this is debug information.')
#         logger.info('this is info information.')
#         logger.warn('this is warn information.')
#         logger.error('this is error information.')
#         logger.critical('this is critical information.')
        
#         if request.user == 'admin':
#             return Response({'message': 'user is belong to superuser. ' + logger})
#         return Response(
#                 {'data': self.serializer_class(cu, many=True).data},
#                 status=status.HTTP_200_OK
#             )