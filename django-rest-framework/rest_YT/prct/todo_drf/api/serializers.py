from rest_framework import serializers
from .models import Task #this is a model to serialize


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    
