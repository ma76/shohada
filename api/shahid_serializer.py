from rest_framework import serializers
from .model import ShahidModel
# Define Shahid-Serializer
class ShahidSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShahidModel
        fields = ['name','description','imageUrl','born_date','shahadat_date']

