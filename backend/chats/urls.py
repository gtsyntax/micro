from django.urls import path
from .api import user_chats, chat_details, send_chat_message

urlpatterns = [
        path('', user_chats, name='user-chats'),
        path('<uuid:chat_id>/', chat_details, name='chat-details'),
        path('<uuid:chat_id>/send-chat/', send_chat_message, name='send-chat-message'),
]      
