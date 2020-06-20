from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    activities = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id','real_name','tz','activities']

    def get_activities(self, request):
        user_activity = Activity.objects.filter(user=request)
        return ActivitySerializer(user_activity, many=True).data

    


class ActivitySerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')
    end_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')
    class Meta:
        model = Activity
        fields = ['start_time', 'end_time']
