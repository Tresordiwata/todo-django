from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer.data):
    class Meta:
        model=User
        fields='__all__'