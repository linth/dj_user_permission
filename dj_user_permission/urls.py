"""dj_user_permission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from users.views import CustomUserList
from users.views import UserList, UserDetail, user_list, user_detail
from gen_faker_data.views import gen_faker_user, gen_faker_extend_user


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', CustomUserList.as_view(), name='CustomUserList'),
    path('extend_user/', include('extend_user.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('users/<str:message>/', view=UserList.as_view()),
    path('users/<int:pk>', view=UserDetail.as_view()),

    path('users-fbv/', view=user_list, name='user-list'),
    path('users-fbv/<int:pk>/', view=user_detail, name='user-detail'),

    path('gen_faker_user/', view=gen_faker_user, name='gen_faker_user'),
    path('gen_faker_extend_user/', view=gen_faker_extend_user, name='gen_faker_extend_user'),
]
