import os
from datetime import timedelta

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    # Secret key - change this in production!
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'windows-dev-key-2024-autotech'
    
    # Database - SQLite for Windows (easy setup)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"sqlite:///{os.path.join(BASE_DIR, 'data', 'automotive_blog.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload settings for Windows
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # AI API Keys (optional for basic setup)
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')