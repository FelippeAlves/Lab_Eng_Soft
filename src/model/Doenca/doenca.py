from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doencas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True, nullable=False)
    sintomas = db.Column(db.String(1000), nullable=False)