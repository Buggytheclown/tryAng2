from rest_framework import serializers
from myLogger.models import myLogger, myLoggerGroup


class myLoggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myLogger
        fields = ('id', 'type', 'error', 'message')


class myLoggerGroupSerializer(serializers.HyperlinkedModelSerializer):
    logs = myLoggerSerializer(many=True)

    class Meta:
        model = myLoggerGroup
        fields = ('id', 'timestamp', 'title', 'logs')
