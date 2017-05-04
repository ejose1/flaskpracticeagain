from flask import Flask
from flask_sqlalchemy import SQLALchemy
from app import views, models

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
