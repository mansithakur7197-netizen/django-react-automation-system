from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Task, DataPoint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user','display_name','bio']

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id','title','description','owner','status','created_at','updated_at']

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ['id','name','value','ts','meta']
