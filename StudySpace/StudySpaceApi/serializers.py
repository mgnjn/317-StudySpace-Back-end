from rest_framework import serializers
from .models import Group, Group_User, User, Chats, Responses, Friends, Posts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lastName', 'email', 'password', 'registration_date', 'interest1','interest2','interest3','program','picture')