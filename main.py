import os
import sys 

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from src.controller.doenca.doencaController import doencaBlueprint 
from src.controller.incidencia.incidenciaController import incidenciaBlueprint 
from src.controller.Tabela.tabelaController import tabelaBlueprint
from src.controller.Grafico.graficoController import graficoBlueprint
from src.model.Doenca.doenca import db as doenca_db
from src.model.Incidencia.incidencia import db as incidencia_db

load_dotenv(find_dotenv())

template_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'src')
template_dir = os.path.join(template_dir, 'view')

app = Flask(__name__, template_folder=template_dir, static_folder=template_dir )

_USERNAME = os.getenv('MARIA_USERNAME')
_PASSWORD = os.getenv('MARIA_PASSWORD')
_DATABASE = os.getenv('MARIA_DATABASE')
_HOST = os.getenv('MARIA_HOST')
_PORT = os.getenv('MARIA_PORT')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

doenca_db.init_app(app)
incidencia_db.init_app(app)

app.register_blueprint(doencaBlueprint)
app.register_blueprint(incidenciaBlueprint)
app.register_blueprint(tabelaBlueprint)
app.register_blueprint(graficoBlueprint)

def init_db(appFlask):
    db = SQLAlchemy(appFlask)
    engine = db.create_engine(f'mysql+pymysql://{_USERNAME}:{_PASSWORD}@{_HOST}:{_PORT}', {})
    try:
        engine.execute(f"CREATE DATABASE {_DATABASE}") 
    except Exception as error:
        print(error)
        pass
    
    with appFlask.app_context():
        doenca_db.create_all()
        incidencia_db.create_all()

@app.route('/')
def home():
    return render_template('Home/home.html', title='Pagina Inicial')



if __name__ == "__main__":
    if 'init_db' in sys.argv:
        init_db(app)
    app.run()