from rest_framework import serializers
from .models import Group, Group_User, User, Chats, Responses, Friends, Posts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'password', 'registration_date', 'interest1','interest2','interest3','program','picture', 'online_status')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('groupName','description','picture')

class GroupUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group_User
        fields = ('user_id','group_id')

class ChatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chats
        fields = ('sender','recipient','message','timestamp')

class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responses
        fields = ('post_id','response_id','time','upvotes','body')

class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friends
        fields = ('user_id','friend_id','status')

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('group_id','author','upvotes','title','time','body','picture')

