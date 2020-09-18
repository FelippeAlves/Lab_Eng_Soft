from flask import Flask

app = Flask(__name__)

@app.route('/')
def primeira_entrega():
    return '''
    <h1>
        <p>Sistema de Coleta e Visualização de Dados Epidemiológicos</p>
        <p>Felippe Alves de Paula - 1460481821027</p>
        <p>Fabricio Galende Marques de Carvalho</p>
    </h1>
    '''

if __name__ == "__main__":
    app.run()