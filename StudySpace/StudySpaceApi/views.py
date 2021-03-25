from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('lastName')
    serializer_class = UserSerializer

    @action(detail=False)
    def interest1(self, request, *args, **kwargs):
        user_id = request.GET.get('id')
        user = self.queryset.get(id=user_id)
        return Response(user.interest1)
