#This is the file where all the Views of our API exist.
#I have created classes ending with List for GET and POST requests.
#I have creared classes ending with Detail to get the entry that needs to be updated and the PUT functionality is present in this class.
#EXCEPTION HANDLING has been implemented in all the classes with respective HTTP status that covers all the test cases.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *


#HOUSE CLASSES
class HouseList(APIView):
    def get(self,request):
        model = House.objects.all()
        serializer = HouseSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer= HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HouseDetail(APIView):
    def get(self,request,name):
        try:
            model =  House.objects.get(name=name)
        except House.DoesNotExist:
            return Response(f'House with address {name} is not found in the database.', status=status.HTTP_404_NOT_FOUND)
        serializer= HouseSerializer(model)
        return Response(serializer.data)

    def put(self,request,name):
        try:
            model = House.objects.get(name=name)
        except House.DoesNotExist:
            return Response(f'House with address {name} is not found in the database.',status=status.HTTP_404_NOT_FOUND)
        serializer= HouseSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#THERMOSTAT CLASSES
class ThermostatList(APIView):
    def get(self,request,name):
        house= House.objects.get(name=name)
        model = house.thermostats.all()
        serializer= ThermostatSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer= ThermostatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThermostatDetail(APIView):
    def get(self,request,name,name2):
        try:
            house = House.objects.get(name=name)
            model = house.thermostats.get(name=name2)
        except Thermostat.DoesNotExist:
            return Response(f'Thermostat {name} is not found in the database.', status=status.HTTP_404_NOT_FOUND)
        serializer= ThermostatSerializer(model)
        return Response(serializer.data)

    def put(self,request,name,name2):
        try:
            house = House.objects.get(name=name)
            model = Thermostat.objects.get(name=name2)
        except Thermostat.DoesNotExist:
            return Response(f'Thermostat {name} is not found in the database.',status=status.HTTP_404_NOT_FOUND)
        serializer= ThermostatSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#ROOM CLASSES
class RoomList(APIView):
    def get(self, request,name):
            house = House.objects.get(name=name)
            model = house.rooms.all()
            serializer = RoomSerializer(model, many=True)
            return Response(serializer.data)

    def post(self, request):
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetail(APIView):
    def get(self, request, name,name2):
        try:
            house = House.objects.get(name=name)
            model = house.rooms.get(name=name2)
        except Room.DoesNotExist:
            return Response(f'Room {name} is not found in the database.',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = RoomSerializer(model)
        return Response(serializer.data)

    def put(self, request, name,name2):
        try:
            house = House.objects.get(name=name)
            model = house.rooms.get(name=name2)
        except Room.DoesNotExist:
            return Response(f'Room {name} is not found in the database.',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = RoomSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#LIGHT CLASSES
class LightList(APIView):
    def get(self,request,name,name2):
        house = House.objects.get(name=name)
        room_model = house.rooms.all()
        room = Room.objects.get(name=name2)
        model = room.lights.all()
        serializer= LightSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer= LightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LightDetail(APIView):
    def get(self,request,name,name2,name3):
        try:
            house = House.objects.get(name=name)
            room = Room.objects.get(name=name2)
            model = room.lights.get(name=name3)
        except Light.DoesNotExist:
            return Response(f'Light {name} is not found in the database.', status=status.HTTP_404_NOT_FOUND)
        serializer= LightSerializer(model)
        return Response(serializer.data)

    def put(self,request,name,name2,name3):
        try:
            house = House.objects.get(name=name)
            room = Room.objects.get(name=name2)
            model = room.lights.get(name=name3)
        except Light.DoesNotExist:
            return Response(f'Light {name} is not found in the database.',status=status.HTTP_404_NOT_FOUND)
        serializer= LightSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


