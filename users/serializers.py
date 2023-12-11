from rest_framework import serializers
from django.contrib.auth.models import User
# from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'username', 'first_name', 'last_name', 'is_active']


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'

