from rest_framework import serializers
from .models import User,PostUser

class UserSerializer(serializers.ModelSerializer.data):
    class Meta:
        model=User
        fields='__all__'
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostUser
        fields = "__all__"