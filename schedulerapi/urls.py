from django.conf.urls import url, include
from rest_framework import routers
from schedulerapi import views
from schedulerapi.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Items', views.ItemViewSet)
router.register(r'Picks', views.PickViewSet)
router.register(r'Randomize', views.RandomizeViewSet, base_name='Item')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]