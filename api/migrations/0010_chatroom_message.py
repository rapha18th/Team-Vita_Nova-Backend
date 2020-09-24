# Generated by Django 3.1.1 on 2020-09-24 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200917_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('is_group_chat', models.BooleanField(default=False)),
                ('last_interaction', models.DateTimeField(auto_now_add=True)),
                ('notice_by_users', models.ManyToManyField(related_name='chat_room_noticed', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='chat_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chatroom')),
                ('read_by_users', models.ManyToManyField(related_name='read_messages', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]