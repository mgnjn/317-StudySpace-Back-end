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
    def groups(self, request, *args, **kwargs):
        user_id = request.GET.get('id')
        return Response(GroupUserViewSet.queryset.filter(user_id=user_id).values_list('group_id',flat=True))
    
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

    @action(detail=False)
    def topGroups(self, request,*args, **kwargs):
        user_id = request.GET.get('id')
        user = UserViewSet.queryset.get(id=user_id)
        group_match = {}
        groups = GroupUserViewSet.queryset.filter(user_id=user_id).values_list("group_id",flat=True)
        for i in self.queryset.values_list('id', flat=True):
            if i in groups:
                pass
            else:
                tags = self.queryset.filter(id=i).values_list('tags', flat=True)[0].split(',')
                matches = 0
                for j in tags:
                    
                    if j == user.interest1:
                        matches += 1
                    elif j == user.interest2:
                        matches += 1
                    elif j == user.interest3:
                        matches += 1
                group_match[i] = matches
        
        group_match = sorted(group_match, key=group_match.get, reverse=True)
        
        
        
        
        
        return Response([i for i in group_match[:5]])



class GroupUserViewSet(viewsets.ModelViewSet):
    queryset = Group_User.objects.all().order_by('group_id')
    serializer_class = GroupUserSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('group_id')
    serializer_class = PostsSerializer

    @action(detail=False)
    def topPosts(self, request,*args, **kwargs):
        user_id = request.GET.get('id')
        groups = GroupUserViewSet.queryset.filter(user_id=user_id).values_list('group_id',flat=True)
        
        for i in range(len(groups)):
            if i == 0:
                posts = self.queryset.filter(group_id=groups[i])
            else:
                posts = posts | self.queryset.filter(group_id=groups[i])
        posts = posts.order_by('upvotes')
        serializer_context = {
            'request': request,
        }
        ser = PostsSerializer(posts,many=True,context=serializer_context)
        return Response(ser.data)


class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all().order_by('friend_id')
    serializer_class = FriendsSerializer

    @action(detail=False)
    def friendsOnline(self, request,*args, **kwargs):
        user_id = request.GET.get('user_id')
        friends = self.queryset.filter(user_id=user_id).values_list('friend_id',flat=True)

        for i in range(len(friends)):
            if i == 0:
                online = UserViewSet.queryset.filter(id=friends[i]).filter(online_status=True)
            else:
                online = online | UserViewSet.queryset.filter(id=friends[i]).filter(online_status=True)
        
        return Response(online.values_list('id',flat=True))

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Responses.objects.all().order_by('post_id')
    serializer_class = ResponseSerializer

    @action(detail=False)
    def responsesPost(self, request,*args, **kwargs):
        post_id = request.GET.get('post_id')
        serializer_context = {
            'request': request,
        }
        responses = self.serializer_class(self.queryset.filter(post_id=post_id), many=True,context=serializer_context)
        return Response(responses.data)


class ChatsViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all().order_by('recipient')
    serializer_class = ChatsSerializer



# Create identical class for chats


    


