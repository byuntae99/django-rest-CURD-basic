from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import *
from Bapp.models import *


@api_view(['GET'])
def sign_up(request):
    serializers = RoomSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        user  = Room.objects.get(Name = request.data['name'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return Response({'token':token.key,"Name":serializers.data})
    return Response(serializers.errors,status = status.HTTP_201_CREATED)



@api_view(['GET','POST'])
def list_od_data(request):
    if request.method == 'GET':
        room = Room.objects.all() 
        serializers=RoomSerializer(room,many = True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializers = RoomSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])   
def list_of_single(request,pk):
    try:
        room = Room.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = RoomSerializer(room)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = RoomSerializer(room,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)




