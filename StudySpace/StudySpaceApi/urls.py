from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'Groups', views.GroupViewSet)
router.register(r'GroupUser', views.GroupUserViewSet)
router.register(r'Responses',views.ResponseViewSet)
router.register(r'Chats',views.ChatsViewSet)
router.register(r'Posts',views.PostsViewSet)
router.register(r'Friends',views.FriendsViewSet)
# register everything else



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
]