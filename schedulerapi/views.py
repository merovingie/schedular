from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from schedulerapi.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
from schedulerapi.serializers import *
from rest_framework.decorators import list_route
import random
from datetime import date


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

class PickViewSet(viewsets.ModelViewSet):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

class RandomizeViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    querysetHigh = Item.objects.filter(severity='HIGH')
    querysetMedium = Item.objects.filter(severity='MEDIUM')
    querysetLow = Item.objects.filter(severity='LOW')
    print(querysetHigh)
    print(querysetMedium)
    print(querysetLow)
    itemTitleLow = random.choice(querysetLow)
    print(itemTitleLow)
    itemTitleMedium = random.choice(querysetMedium)
    print(itemTitleMedium)
    itemTitleHigh = random.choice(querysetHigh)
    print(itemTitleHigh)

    P = Pick(dayDate = date.today(), itemA = itemTitleHigh, itemB = itemTitleMedium, itemC = itemTitleLow)
    print(Pick.dayDate)
    print(Pick.itemA)
    print(Pick.itemB)
    print(Pick.itemC)
    P.save()


    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})
