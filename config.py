import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_PATH = 16 * 1024 * 1024
