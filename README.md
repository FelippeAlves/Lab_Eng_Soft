Felippe Alves de Paula - 1460481821027

# Requisitos:

- [x] Git instalado - <a href=https://git-scm.com/downloads/>Download Git</a>

- [x] Python 3.6 ou maior - <a href=https://www.python.org/downloads/>Download Python</a>

- [x] Banco de dados MariaDB - <a href=https://mariadb.org/download/>Download MariaBD</a>

# Para Iniciar o projeto:
Necessário clonar o repositório:

```
  git clone https://github.com/FelippeAlves/Lab_Eng_Soft.git
  
  git checkout segunda-entrega

  git pull
```

# Ativando o Virtual Environment:

```
python -m venv env

env\Scripts\activate
```

# Instalando as bibliotecas:

```
pip install -r requirements.txt
```

# Criando o arquivo .env:

Na pasta principal, existe um arquivo chamado: exemploenv, será necessário renomeá-lo para .env e adicionar os parâmetros conforme às credenciais do MariaDB, exemplo:

```
MARIA_USERNAME=root //user adm
MARIA_PASSWORD=1357911 //senha adm
MARIA_DATABASE=dadosdoencas
MARIA_HOST=127.0.0.1
MARIA_PORT=3306
```
# Primeira vez acessando o projeto:

Será necessário utilizar alguns comando para iniciar o projeto pela primeira vez, pois ainda não existe os dados no banco de dados:

```
python wsgi.py init_db
```

Caso já possua os dados no banco de dados, somente é necessário o seguinte comando para iniciar o projeto:

```
python wsgi.py
```

À partir de agora, deverá conter a seguinte mensagem no terminal:

```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Basta abrir a URL para acessar o projeto.
