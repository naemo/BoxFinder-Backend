from .models import Essay, Lead, UserData
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')
    #fake data

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = UserData
        fields = ('pk','email', 'password', 'remember_me')