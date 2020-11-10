from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Incidencias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_doenca = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime(), nullable=False)