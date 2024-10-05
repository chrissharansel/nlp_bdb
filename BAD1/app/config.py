class Config:
    SECRET_KEY = "your-secret-key"
    DEBUG = True
    UPLOAD_FOLDER = '/static/audio'
    ALLOWED_EXTENSIONS = {'wav', 'mp3'}

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
