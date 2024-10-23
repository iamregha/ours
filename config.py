import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))



class Config:
    """Base config."""
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOAD_PATH = 'static/post_images/'
    UPLOAD_FOLDER = 'static/images/profile/'
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
    #SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')#.replace('postgres://', 'postgresql://')

    # First, try to get POSTGRES_URL (used by Vercel)
    db_url = os.getenv('POSTGRES_URL')
    
    # If POSTGRES_URL is not set, fallback to DATABASE_URL
    if not db_url:
        db_url = os.getenv('POSTGRES_URL')

    # Normalize the URL to ensure compatibility
    # Check if the URL uses postgres:// and convert it to postgresql://
    if db_url and db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = db_url
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URL set for Flask application")


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "")



#print("DATABASE_URL:", os.getenv('DATABASE_URL'))
