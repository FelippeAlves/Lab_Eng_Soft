import json

from flask import Blueprint, render_template, request, current_app, Response
from flask_sqlalchemy import SQLAlchemy

from src.model.Doenca.doenca import Doencas


doencaBlueprint = Blueprint('doenca', __name__, url_prefix='/doenca')

@doencaBlueprint.route('/')
def doencaHome():
    return render_template('Doenca/doenca.html')

@doencaBlueprint.route('/save', methods=['POST'])
def save():
    db = SQLAlchemy(current_app)

    obj = request.json

    newDoenca = Doencas(**obj)

    with current_app.app_context():
        db.session.add(newDoenca)
        db.session.commit()

    res = json.dumps({'msg': 'Doênça cadastrada'})
    return Response(res, mimetype='application/json', status=200)

def getDoencas():
    try:
        db = SQLAlchemy(current_app)

        doencas = Doencas.query.all()
        if not doencas:
            raise "Sem dados de doênças"

        doencas = list(map(lambda x: x.nome, doencas))

        return doencas

    except SQLAlchemyError as error:
        res = json.dumps({"Erro": str(error.__dict__['orig'])})
        print(res)
        raise None
    
    except Exception as error:
        res = json.dumps({"Erro": str(error)})
        print(res)
        raise None