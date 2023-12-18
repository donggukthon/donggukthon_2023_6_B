from rest_framework import serializers
from .models import trashCans

#class reportList(serializers.ModelSerializer):
#    class Meta:
#        model = trashCans
#        fields = ['address', 'picture', 'information', 'complaincount',]

class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = trashCans
        fields = '__all__'