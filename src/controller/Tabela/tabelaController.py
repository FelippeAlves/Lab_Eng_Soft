from flask import Blueprint, render_template

tabelaBlueprint = Blueprint('tabela', __name__, url_prefix='/tabela')

@tabelaBlueprint.route('/')
def homeTabela():
    
    return render_template('Tabela/tabela.html')