from django.shortcuts import render
from .serializers import UserSerializer, GroupSerializer, GroupUserSerializer, PostsSerializer, FriendsSerializer, ResponseSerializer, ChatsSerializer
from .models import Group, Group_User, User, Chats, Responses, Friends, Posts
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from itertools import chain
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('lastName')
    serializer_class = UserSerializer
    @action(detail=False)
    def firstName(self, request, *args, **kwargs):
        user_id=request.GET.get('id')
        user=self.queryset.get(id=user_id)
        return Response(user.firstName)

    @action(detail=False)
    def lastName(self, request, *args, **kwargs):
        user_id=request.GET.get('id')
        user=self.queryset.get(id=user_id)
        return Response(user.lastName)
    
    @action(detail=False)
    def email(self, request, *args, **kwargs):
        user_id=request.GET.get('id')
        user=self.queryset.get(id=user_id)
        return Response(user.email)

    @action(detail=False)
    def password(self, request, *args, **kwargs):
        user_id=request.GET.get('id')
        user=self.queryset.get(id=user_id)
        return Response(user.password)
    
    @action(detail=False)
    def registration_date(self, request, *args, **kwargs):
        user_id=request.GET.get('id')
        user=self.queryset.get(id=user_id)
        return Response(user.registration_date)


    @action(detail=False)
    def interest(self, request,*args, **kwargs):
        user_id = request.GET.get('id')
        user = self.queryset.get(id=user_id)
        
        return Response([user.interest1,user.interest2,user.interest3])
    
    @action(detail=False)
    def program(self, request, *args, **kwargs):
        user_id=request.GET.get('id')
        user=self.queryset.get(id=user_id)
        return Response(user.program)


    @action(detail=False)
    def matches(self, request,*args, **kwargs):
        user_id = request.GET.get('id')
        user = self.queryset.get(id=user_id)
        userList=self.queryset.filter(interest1=user.interest1).filter(interest2=user.interest2).filter(interest3=user.interest3).exclude(id=user_id).values_list('id', flat=True)
        userList2=self.queryset.filter(interest1=user.interest1).filter(interest2=user.interest2).exclude(interest3=user.interest3).exclude(id=user_id).values_list('id', flat=True)
        userList3=self.queryset.filter(interest1=user.interest1).exclude(interest2=user.interest2).exclude(interest3=user.interest3).exclude(id=user_id).values_list('id', flat=True)
        userList = list(chain(userList,userList2,userList3))
        return Response(userList)
    #Create get for all the parameters

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('groupName')
    serializer_class = GroupSerializer

class GroupUserViewSet(viewsets.ModelViewSet):
    queryset = Group_User.objects.all().order_by('group_id')
    serializer_class = GroupUserSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('group_id')
    serializer_class = PostsSerializer

class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all().order_by('friend_id')
    serializer_class = FriendsSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Responses.objects.all().order_by('post_id')
    serializer_class = ResponseSerializer

class ChatsViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all().order_by('recipient')
    serializer_class = ChatsSerializer



# Create identical class for chats


    


