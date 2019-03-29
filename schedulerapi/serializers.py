from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'severity', 'title', 'description', 'timeNow', 'timeScheduled', 'weekly', 'yearly', 'monthly', 'daily')


class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = ('dayDate', 'itemA', 'isDoneA', 'itemB', 'isDoneB', 'itemC', 'isDoneC')