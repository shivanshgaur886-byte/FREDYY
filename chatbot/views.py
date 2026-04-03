import json
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import openai

from .models import ChatConversation, ChatMessage

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY', '')


@login_required
def chat_home(request):
    """Display chat interface"""
    conversations = ChatConversation.objects.filter(user=request.user)
    
    # Get latest conversation or create new one
    current_conversation = conversations.first()
    if not current_conversation:
        current_conversation = ChatConversation.objects.create(
            user=request.user,
            title='New Chat'
        )
    
    context = {
        'conversations': conversations,
        'current_conversation': current_conversation,
    }
    return render(request, 'chatbot/chat.html', context)


@login_required
def get_conversation(request, conversation_id):
    """Get specific conversation"""
    conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)
    messages = conversation.messages.all()
    
    context = {
        'conversations': ChatConversation.objects.filter(user=request.user),
        'current_conversation': conversation,
        'messages': messages,
    }
    return render(request, 'chatbot/chat.html', context)


@login_required
@require_http_methods(['POST'])
def send_message(request):
    """Send message and get AI response"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        conversation_id = data.get('conversation_id')

        if not user_message:
            return JsonResponse({'error': 'Empty message'}, status=400)

        # Get or create conversation
        if conversation_id:
            conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)
        else:
            conversation = ChatConversation.objects.create(user=request.user)

        # Save user message
        user_msg = ChatMessage.objects.create(
            conversation=conversation,
            role='user',
            content=user_message
        )

        # Get conversation history
        messages_history = []
        for msg in conversation.messages.all().order_by('created_at'):
            messages_history.append({
                'role': msg.role,
                'content': msg.content
            })

        # Call OpenAI API
        if not openai.api_key:
            return JsonResponse({'error': 'OpenAI API key not configured'}, status=500)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_history,
            temperature=0.7,
            max_tokens=1000
        )

        assistant_message = response.choices[0].message['content']

        # Save assistant response
        ai_msg = ChatMessage.objects.create(
            conversation=conversation,
            role='assistant',
            content=assistant_message
        )

        # Update conversation title if first message
        if conversation.messages.count() == 2:  # user + assistant
            title = user_message[:50]
            if len(user_message) > 50:
                title += '...'
            conversation.title = title
            conversation.save()

        return JsonResponse({
            'success': True,
            'conversation_id': conversation.id,
            'user_message': user_msg.id,
            'assistant_message': ai_msg.id,
            'response': assistant_message,
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
@require_http_methods(['POST'])
def new_conversation(request):
    """Create new conversation"""
    conversation = ChatConversation.objects.create(user=request.user)
    return JsonResponse({
        'success': True,
        'conversation_id': conversation.id
    })


@login_required
@require_http_methods(['DELETE'])
def delete_conversation(request, conversation_id):
    """Delete a conversation"""
    conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)
    conversation.delete()
    return JsonResponse({'success': True})
