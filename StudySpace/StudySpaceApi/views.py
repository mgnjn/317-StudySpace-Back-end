from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
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
    def interest(self, request,*args, **kwargs):
        user_id = request.GET.get('id')
        user = self.queryset.get(id=user_id)
        
        return Response([user.interest1,user.interest2,user.interest3])

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


