from app.models.models import conexao
from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    lista = list(range(10))
    return render_template('index.html', nome = 'tiago', lista = lista)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login', methods=['POST'])
def login():
    # args no lugar no form aceita por metodo GET
    usuario = request.form.get('usuario').strip()
    senha = request.form.get('senha').strip()

    if usuario and senha:
        teste = conexao(host = 'us-cdbr-east-06.cleardb.net', 
                    user = 'b6ac0eeaf6adcc', 
                    password = '5d88e207', 
                    database='heroku_bf31a8a8a28ff60')

        string = (teste.ver('login'))
   
    return render_template('login.html', user = usuario, password = senha, bd = string)