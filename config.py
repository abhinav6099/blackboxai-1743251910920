import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUDIO_UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'public/audio')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB upload limit