from django.contrib import admin
from .models import Group, Group_User, User, Chats, Responses, Friends, Posts
# Register your models here.

admin.site.register(Group)
admin.site.register(Group_User)
admin.site.register(User)
admin.site.register(Chats)
admin.site.register(Responses)
admin.site.register(Friends)
admin.site.register(Posts)