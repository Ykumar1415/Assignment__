from flask_sqlalchemy import SQLAlchemy
from app import app
from config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(20))
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
