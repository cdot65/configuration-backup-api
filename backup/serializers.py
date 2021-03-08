from rest_framework import serializers
from backup.models import Backup, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class BackupSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='backup-highlight', format='html')

    class Meta:
        model = Backup
        fields = ['url', 'id', 'highlight', 'owner',
                  'hostname', 'config', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    backups = serializers.HyperlinkedRelatedField(many=True, view_name='backup-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'backups']
