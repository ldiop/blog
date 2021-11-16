from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from ..ftp.models.models import T_user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

#class FtpuserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = T_user
#        fields = ('ftpUsername', 'ftpPassword', 'actif', 'ftpHomeDir', 'nom', 'societe', 'telephone', 'contact_interne', 'dateExpiration')
