from Users.models import User, Activity
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from Users.serializers import UserSerializer, ActivitySerializer

class UsersList(viewsets.ViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response({
            'ok': True,
            'members': serializer.data
            })