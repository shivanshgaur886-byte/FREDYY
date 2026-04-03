from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chat_home, name='home'),
    path('conversation/<int:conversation_id>/', views.get_conversation, name='conversation'),
    path('api/send/', views.send_message, name='send_message'),
    path('api/new/', views.new_conversation, name='new_conversation'),
    path('api/delete/<int:conversation_id>/', views.delete_conversation, name='delete_conversation'),
]
