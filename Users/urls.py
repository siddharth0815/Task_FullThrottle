from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UsersList

router = routers.DefaultRouter()
router.register('users', UsersList)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]