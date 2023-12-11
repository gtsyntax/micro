from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from .serializers import ChatSerializer, ChatMessageSerializer, ChatDetailSerializer
from .models import Chat


@api_view(['GET'])
def user_chats(request):
    chats = Chat.objects.filter(participants=request.user)
    serializer = ChatSerializer(chats, many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def chat_details(request, chat_id):
    chat = get_object_or_404(Chat, participants=request.user, pk=chat_id) 
    serializer = ChatDetailSerializer(chat)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def send_chat_message(request, chat_id):
    chat = get_object_or_404(Chat, participants=request.user, pk=chat_id) 
    serializer = ChatMessageSerializer(data=request.data)

    #recipient = [participant for participant in chat.participants.all() if participant != request.user]
    for participant in chat.participants.all():
        if participant != request.user:
            recipient = participant

    if serializer.is_valid():
        serializer.save(
                chat=chat,
                sender=request.user,
                recipient=recipient,
                content=serializer.validated_data['content'],
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
