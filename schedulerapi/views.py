from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from schedulerapi.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from .models import *
from schedulerapi.serializers import *
from rest_framework.decorators import list_route, action
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

    @action(detail=True)
    def setA(self, request, **kwargs):
        Pick = self.get_object()
        serializer = PickSerializer(Pick)
        print(Pick)
        Pick.isDoneA = True
        Pick.save()
        return Response(serializer.data)

    @action(detail=True)
    def setB(self, request, **kwargs):
        Pick = self.get_object()
        serializer = PickSerializer(Pick)
        print(Pick)
        Pick.isDoneB = True
        Pick.save()
        return Response(serializer.data)

    @action(detail=True)
    def setC(self, request, **kwargs):
        Pick = self.get_object()
        serializer = PickSerializer(Pick)
        print(Pick)
        Pick.isDoneC = True
        Pick.save()
        return Response(serializer.data)


class RandomizeViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    @action(detail=False)
    def RandomAction(self, request, **kwargs):
        querysetHigh = Item.objects.filter(severity='HIGH')
        querysetMedium = Item.objects.filter(severity='MEDIUM')
        querysetLow = Item.objects.filter(severity='LOW')
        serializer = ItemSerializer(Item)

        print(querysetHigh)
        print(querysetMedium)
        print(querysetLow)

        itemTitleLow = random.choice(querysetLow)
        print(itemTitleLow)
        itemTitleMedium = random.choice(querysetMedium)
        print(itemTitleMedium)
        itemTitleHigh = random.choice(querysetHigh)
        print(itemTitleHigh)

        P = Pick(dayDate=date.today(), itemA=itemTitleHigh, itemB=itemTitleMedium, itemC=itemTitleLow)
        print(Pick.dayDate)
        print(Pick.itemA)
        print(Pick.itemB)
        print(Pick.itemC)
        P.save()
        return Response()

    # querysetHigh = Item.objects.filter(severity='HIGH')
    # querysetMedium = Item.objects.filter(severity='MEDIUM')
    # querysetLow = Item.objects.filter(severity='LOW')
    # print(querysetHigh)
    # print(querysetMedium)
    # print(querysetLow)
    # itemTitleLow = random.choice(querysetLow)
    # print(itemTitleLow)
    # itemTitleMedium = random.choice(querysetMedium)
    # print(itemTitleMedium)
    # itemTitleHigh = random.choice(querysetHigh)
    # print(itemTitleHigh)
    #
    # P = Pick(dayDate = date.today(), itemA = itemTitleHigh, itemB = itemTitleMedium, itemC = itemTitleLow)
    # print(Pick.dayDate)
    # print(Pick.itemA)
    # print(Pick.itemB)
    # print(Pick.itemC)
    # P.save()
    # queryset = {}






class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})
