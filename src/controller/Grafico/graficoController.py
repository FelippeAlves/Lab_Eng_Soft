from flask import Blueprint, render_template

graficoBlueprint = Blueprint('grafico', __name__, url_prefix='/grafico')

@graficoBlueprint.route('/')
def homeGrafico():
    
    return render_template('Grafico/grafico.html')