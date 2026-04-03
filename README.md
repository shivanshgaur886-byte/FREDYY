# 🤖 FREDDY - AI ChatBot & Task Manager

[![Django](https://img.shields.io/badge/Django-5.2.12-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> A modern, feature-rich Django application combining task management with an advanced AI chatbot powered by OpenAI's GPT-3.5 Turbo.

## ✨ Features

### 🤖 **FREDDY AI ChatBot**
- **Conversational AI** powered by OpenAI GPT-3.5 Turbo
- **Multi-conversation support** - Manage multiple chat sessions
- **Real-time responses** with typing indicators
- **Context-aware conversations** - Remembers chat history
- **Modern UI** with emojis and animations
- **Responsive design** - Works on all devices

### 📋 **Task Management System**
- **User authentication** and secure login
- **Create, read, update, delete** tasks
- **Task status tracking** (Pending, In Progress, Completed)
- **User-specific tasks** with privacy
- **Clean, intuitive interface**

### 🎨 **Advanced UI/UX**
- **Gemini-inspired design** with modern aesthetics
- **Emoji-rich interface** for better user experience
- **Smooth animations** and transitions
- **Dark/light mode ready** components
- **Mobile-responsive** layout

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Git
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/shivanshgaur886-byte/FREDDY.git
cd FREDDY
```

2. **Create virtual environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirement.txt
```

4. **Set up environment variables:**
```bash
# Create .env file or set environment variable
# Option 1: Create .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env

# Option 2: Set environment variable
export OPENAI_API_KEY="your-api-key-here"
```

5. **Run database migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Start the development server:**
```bash
python manage.py runserver
```

8. **Open in browser:**
- Main app: http://localhost:8000/
- FREDDY ChatBot: http://localhost:8000/chat/
- Admin panel: http://localhost:8000/admin/

## 📖 Usage

### 🤖 Using FREDDY ChatBot
1. **Login/Register** with your account
2. **Navigate to** `/chat/` URL
3. **Start chatting!** FREDDY will respond intelligently
4. **Create new conversations** using the ➕ button
5. **Switch between conversations** from the sidebar

### 📋 Task Management
1. **Login** to access your dashboard
2. **Add new tasks** with title and description
3. **Update task status** as you progress
4. **Mark tasks complete** when done
5. **Delete tasks** you no longer need

## 🛠️ Configuration

### OpenAI Settings
Edit `chatbot/config.py` or environment variables:

```python
CHAT_MODEL = "gpt-3.5-turbo"  # or "gpt-4"
TEMPERATURE = 0.7             # Creativity (0.0-2.0)
MAX_TOKENS = 1000             # Response length
```

### Django Settings
Key settings in `config/settings.py`:
- `DEBUG = False` for production
- Database configuration
- Static files settings
- Security settings

## 📁 Project Structure

```
FREDDY/
├── chatbot/              # 🤖 AI ChatBot app
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── static/          # CSS/JS (if added)
│   ├── models.py        # ChatConversation, ChatMessage
│   ├── views.py         # API endpoints
│   ├── urls.py          # URL routing
│   └── config.py        # OpenAI settings
├── tasks/               # 📋 Task management app
│   ├── models.py        # Task model
│   ├── views.py         # CRUD operations
│   ├── templates/       # Task templates
│   └── forms.py         # Task forms
├── config/              # ⚙️ Django settings
├── templates/           # 📄 Global templates
├── static/             # 🎨 Static files
├── db.sqlite3          # 🗄️ Database
├── manage.py           # 🚀 Django CLI
├── requirement.txt     # 📦 Dependencies
└── README.md           # 📖 This file
```

## 🔧 API Endpoints

### ChatBot API
- `GET /chat/` - Chat interface
- `POST /chat/api/send/` - Send message & get AI response
- `POST /chat/api/new/` - Create new conversation
- `DELETE /chat/api/delete/<id>/` - Delete conversation

### Task Management
- `GET /` - Task dashboard
- `POST /add/` - Add new task
- `POST /update/<id>/` - Update task
- `POST /delete/<id>/` - Delete task

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-name`
3. **Commit** changes: `git commit -m 'Add feature'`
4. **Push** to branch: `git push origin feature-name`
5. **Open** a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for GPT-3.5 Turbo API
- **Django** framework
- **Bootstrap** for UI components
- **GitHub** for hosting

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/shivanshgaur886-byte/FREDDY/issues)
- **Discussions:** [GitHub Discussions](https://github.com/shivanshgaur886-byte/FREDDY/discussions)

## 🎯 Future Enhancements

- [ ] **Voice input/output** for hands-free chatting
- [ ] **File upload** and analysis capabilities
- [ ] **Multi-language support**
- [ ] **Advanced conversation analytics**
- [ ] **Integration with external APIs**
- [ ] **Mobile app** version
- [ ] **Real-time collaboration** features

---

**Made with ❤️ by Shivansh Gaur**

**FREDDY is ready to chat! 🤖✨**