from rest_framework import serializers
from .models import Declaration
from user.models import User
from report.models import trashCans

class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.get(pk=1)
        trashCans = trashCans.objects.get(pk=1)