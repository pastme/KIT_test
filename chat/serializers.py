import os
from rest_framework import serializers
from chat.models import Message

class MessageSerializer(serializers.ModelSerializer):
    from_user = serializers.ReadOnlyField(source='from_user.username')
    file_name = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
        
    class Meta:
        model = Message
        fields = ('text','timestamp','from_user','file_name','file_url')

    def get_file_name(self,obj):
        name = os.path.basename(obj.file.name) if obj.file else ''
        return name

    def get_file_url(self,obj):
        url = obj.file.url if obj.file else ''
        return url


class MessageShortSerializer(MessageSerializer):

    class Meta:
        model = Message
        fields = ('text','file')
