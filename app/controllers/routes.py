from app.models.models import conexao
from flask import render_template, request, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

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

        if teste.consultar('login', ['email', 'senha'], [usuario, senha]):
            string = (teste.ver('login'))
            return render_template('login.html', user = usuario, password = senha, bd = string), teste.sair()

        else:
            return render_template('index.html')

    return render_template('index.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/conta_nova')
def conta_nova():
    return render_template('conta_nova.html')

