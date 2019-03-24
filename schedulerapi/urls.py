from django.conf.urls import url, include
from rest_framework import routers
from schedulerapi import views
from schedulerapi.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Items', views.ItemViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]