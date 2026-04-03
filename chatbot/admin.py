from django.contrib import admin
from .models import ChatConversation, ChatMessage


@admin.register(ChatConversation)
class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    search_fields = ['user__username', 'title']
    list_filter = ['created_at', 'user']


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'role', 'created_at']
    search_fields = ['conversation__title', 'content']
    list_filter = ['role', 'created_at']
