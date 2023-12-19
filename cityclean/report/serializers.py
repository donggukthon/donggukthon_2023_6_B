from rest_framework import serializers
from .models import trashCans
from user.models import User

class TrashCanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = trashCans
        fields = ['id', 'address', 'picture', 'information', 'complaincount',]

    def create(self, validated_data):
        user = User.objects.get(pk=1)

class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = trashCans
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.get(pk=1)

class TrashCansListSerializer(serializers.ModelSerializer):
    class Meta:
        model = trashCans
        fields = ['id', 'latitude', 'longitude']

    def create(self, validated_data):
        user = User.objects.get(pk=1)
    