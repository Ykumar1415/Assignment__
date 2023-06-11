import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SECRET_KEY = os.getenv('APP_SECRET_KEY')
