# 🤖 Django ChatBot Setup Guide

## Installation Steps

### 1. Install Required Dependencies
```bash
pip install -r requirement.txt
```

The chatbot needs the OpenAI library. Make sure you have:
```
openai==0.28.1
```

### 2. Set Up OpenAI API Key
You need an OpenAI API key to use the chatbot. Get it from https://platform.openai.com/api-keys

**On Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

**On Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-api-key-here
```

**On Mac/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 3. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server
```bash
python manage.py runserver
```

### 5. Access the ChatBot
- Go to `http://localhost:8000/chat/`
- Log in with your account
- Start chatting!

---

## Features

✨ **Gemini-like Interface**
- Clean, modern chat interface
- Dark/light mode ready
- Responsive design

💬 **Multi-Conversation Support**
- Create multiple conversations
- Each conversation stored in database
- Easy switching between conversations

🔐 **User-Specific**
- Each user has their own conversations
- Secure authentication required
- Privacy maintained

🚀 **Powered by OpenAI**
- GPT-3.5 Turbo model by default
- Intelligent responses
- Context-aware conversations

---

## File Structure

```
chatbot/
├── migrations/          # Database migrations
├── admin.py            # Django admin configuration
├── apps.py             # App configuration
├── models.py           # ChatConversation & ChatMessage models
├── urls.py             # URL routing
└── views.py            # API endpoints & views

templates/
├── base.html           # Base template
└── chatbot/
    └── chat.html       # Chat interface template
```

---

## Models

### ChatConversation
- Stores conversation sessions
- Linked to user
- Title, creation date, last update

### ChatMessage
- Individual messages in a conversation
- Role: 'user' or 'assistant'
- Timestamp tracking

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/chat/` | Display chat interface |
| GET | `/chat/conversation/<id>/` | Load specific conversation |
| POST | `/chat/api/send/` | Send message & get response |
| POST | `/chat/api/new/` | Create new conversation |
| DELETE | `/chat/api/delete/<id>/` | Delete conversation |

---

## Customization

### Change the AI Model
Edit `views.py` line ~86:
```python
model="gpt-3.5-turbo"  # Change to gpt-4, gpt-4-turbo, etc.
```

### Adjust Temperature (Creativity)
```python
temperature=0.7  # Range: 0.0 (precise) to 2.0 (creative)
```

### Modify Max Tokens
```python
max_tokens=1000  # Adjust response length limit
```

---

## Troubleshooting

### "OpenAI API key not configured"
Make sure you set the `OPENAI_API_KEY` environment variable correctly.

### Migrations Failed
```bash
python manage.py migrate --run-syncdb
```

### Chat Template Not Found
Make sure `templates/chatbot/` directory exists and `base.html` is in `templates/`.

---

## Security Notes

- Never commit your API key to git!
- Keep your `OPENAI_API_KEY` private
- Consider using environment variables from `.env` files
- Use Django's built-in authentication

---

## Next Steps

1. **Add Rate Limiting** - Prevent API spam
2. **Add Streaming** - Show responses as they're generated
3. **Add Search** - Search through conversation history
4. **Add Export** - Export conversations to PDF
5. **Add Customization** - Let users customize system prompts

---

Happy Chatting! 🚀
