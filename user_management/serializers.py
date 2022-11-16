from django.contrib.auth.models import User
from rest_framework import serializers
from user_management.models import Profile
from task.models import Task

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_staff','user_permissions', 'groups', 'is_superuser','username')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        validated_data['username'] = validated_data['email']
        validated_data['is_active'] = True
        user_type = validated_data['user_type']
        del validated_data['user_type']
        user = User.objects.create_user(**validated_data)
        
        Profile.objects.create(i_user=user,user_type=user_type)
        
        return validated_data

    
    def validate_email(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('This email is already taken')
        else:
            return value
    
    def validate_password(self, value):
        if value.isdigit():
            if len(value) == 4:
                return value
            else:
                raise serializers.ValidationError('Please enter 4 digit password')
        else:
            raise serializers.ValidationError('Please enter Numeratic password only')
            


       
class AllUsersSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']

class AllUsersPicsSerializer(serializers.ModelSerializer):
    i_user = AllUsersSerializer()



class AllTask(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
    class Meta:
        model = Task
        fields = ['id','task']
