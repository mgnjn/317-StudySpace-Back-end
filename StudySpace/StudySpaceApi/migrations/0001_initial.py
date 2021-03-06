# Generated by Django 3.1.7 on 2021-03-24 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('picture', models.ImageField(upload_to='group')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySpaceApi.group')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=25)),
                ('registration_date', models.DateTimeField()),
                ('interest1', models.CharField(max_length=20)),
                ('interest2', models.CharField(max_length=20)),
                ('interest3', models.CharField(max_length=20)),
                ('program', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='user')),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySpaceApi.posts')),
                ('response_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StudySpaceApi.responses')),
            ],
        ),
        migrations.CreateModel(
            name='Group_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySpaceApi.group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySpaceApi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1)),
                ('friend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_friend', to='StudySpaceApi.user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_user', to='StudySpaceApi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_recipient', to='StudySpaceApi.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_sender', to='StudySpaceApi.user')),
            ],
        ),
    ]
