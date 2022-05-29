from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Drawing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drawings = serializers.HyperlinkedRelatedField(many=True, view_name='drawing-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'drawings', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DrawingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Drawing
        fields = ['user', 'title', 'submitted_at', 'description', 'votes']
