from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

import logging


class IsOwnerOrReadOnly(permissions.BasePermission):
    ''' Custom permission to only allow owners of an object to edit it. '''
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
    

class ReadOnly(permissions.BasePermission):
    # 只能可以讀
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS        
    
    
class IsOwnerCanRead(permissions.BasePermission):
    # 只能擁有者才可以讀
    logger = logging.getLogger('my-logging')
        
    def has_object_permission(self, request, view, obj):
        
        if obj == request.user:
            self.logger.debug('user is the same.')
            return True
        self.logger.debug('user isn\'t the same')
        return False
    
    
class IsOwnerOrSuperUserCanRead(permissions.BasePermission):
    # 只能擁有者 or super user 才可以讀
    pass