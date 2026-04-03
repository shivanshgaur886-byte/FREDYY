"""
Django ChatBot Configuration

This module provides centralized configuration for the chatbot app.
"""

import os

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

# Chat Model Settings
CHAT_MODEL = os.getenv('CHAT_MODEL', 'gpt-3.5-turbo')
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 1000))
