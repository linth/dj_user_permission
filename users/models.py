from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from django.utils import timezone

# https://docs.djangoproject.com/en/5.0/topics/auth/default/
# from users.managers import CustomUserManager

# AbstractUser

# UserRole = {'admin': 'admin', 'member': 'member'}


# class 


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = None

#     email = models.EmailField(_('email address'), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     # TODO: add fields as follows.
#     # oring_id
#     # group_id
#     # description
#     # role: UserRole
#     # created_at
#     # updated_at

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self) -> str:
#         return self.email

