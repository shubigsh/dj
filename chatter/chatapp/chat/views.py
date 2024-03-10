from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Room, Message

def room(request, room_name):
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room)
    return render(request, 'chat/room.html', {'room_name': room_name, 'messages': messages})