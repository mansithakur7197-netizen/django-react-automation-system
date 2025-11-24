from rest_framework import routers
from .views import UserViewSet, ProfileViewSet, TaskViewSet, DataPointViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'datapoints', DataPointViewSet, basename='datapoint')

urlpatterns = [
    path('', include(router.urls)),
]
