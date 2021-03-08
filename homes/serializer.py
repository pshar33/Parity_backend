


# I have created different serializers for the different models defined in our model.py. These are being called in the views defined in api.py.

from rest_framework import  serializers
from homes.models import *
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class ThermostatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thermostat
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'
