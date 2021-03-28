from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    registration_date = models.DateTimeField()
    interest1 = models.CharField(max_length=20)
    interest2 = models.CharField(max_length=20)
    interest3 = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    picture = models.ImageField(upload_to="user")

    def __str__(self):
        return self.lastName

    

class Friends(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_user")
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_friend") # consider delete function
    status = models.CharField(max_length=1)


class Group(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to="group")

class Posts(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()

class Responses(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    response_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    body = models.TextField()

class Chats(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_sender")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_recipient")
    message = models.TextField()
    timestamp = models.DateTimeField()


class Group_User(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE) # consider delete functionality