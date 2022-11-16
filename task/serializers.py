from django.contrib.auth.models import User
from rest_framework import serializers
from task.models import Task

class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('i_user',)


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','task',)
    
    def update(self, instance, validated_data):
        
        instance.task = validated_data.get('task', instance.task)
        instance.save()
        return instance