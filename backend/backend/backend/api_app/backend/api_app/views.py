from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile, Task, DataPoint
from .serializers import ProfileSerializer, TaskSerializer, DataPointSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('owner').all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # users see only their tasks unless staff
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        qs = Task.objects.filter(owner=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

class DataPointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def recent(self, request):
        qs = self.get_queryset()[:200]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
