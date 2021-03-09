from rest_framework import serializers
from golden.models import Golden
from django.contrib.auth.models import User


class GoldenSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Golden
        fields = ['url', 'id', 'owner', 'hostname', 'golden', 'diff']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    configs = serializers.HyperlinkedRelatedField(many=True, view_name='config-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'configs']
