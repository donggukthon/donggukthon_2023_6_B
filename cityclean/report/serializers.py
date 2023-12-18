from rest_framework import serializers
from .models import trashCans

class TrashCanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = trashCans
        fields = ['address', 'picture', 'information', 'complaincount',]

class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = trashCans
        fields = '__all__'