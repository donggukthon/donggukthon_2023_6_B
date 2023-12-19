from rest_framework import serializers
from .models import Trash
from user.models import User

class TrashListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['id', 'address', 'picture', 'information']

    def create(self, validated_data):
        user = User.objects.get(pk=1)

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['address', 'picture', 'information']

    def create(self, validated_data):
        user = User.objects.get(pk=1)