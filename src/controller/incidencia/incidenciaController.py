import json

from flask import Blueprint, render_template, request, current_app, Response
from flask_sqlalchemy import SQLAlchemy
from src.controller.doenca.doencaController import getDoencas
from sqlalchemy.exc import SQLAlchemyError

from src.model.Incidencia.incidencia import Incidencias
from src.model.Doenca.doenca import Doencas

incidenciaBlueprint = Blueprint('incidencia', __name__, url_prefix='/incidencia')

@incidenciaBlueprint.route('/')
def homeIncidencia():
    try:
        doenca = getDoencas()
    except Exception as error:
        print(error)
        doenca = []

    return render_template('Incidencia/incidencia.html', data={"doenca": doenca})

@incidenciaBlueprint.route('/save', methods=['POST'])
def saveIncidencias():
    try:
        db = SQLAlchemy(current_app)

        obj = request.json

        doenca = Doencas.query.filter_by(nome=obj['selectDoenca']).first()
        newIncidencia = Incidencias(fk_doenca=doenca.id, data=obj['dataIncidencia'])
        
        with current_app.app_context():
            db.session.add(newIncidencia)
            db.session.commit()

        res = json.dumps({'msg': 'Incidência cadastrada'})
        return Response(res, mimetype='application/json', status=200)
        
    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        return Response(res, mimetype='application/json', status=500)
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        return Response(res, mimetype='application/json', status=500)