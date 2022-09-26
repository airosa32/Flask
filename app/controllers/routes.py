from email.policy import default
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
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    
    return render_template('login.html', user = usuario, password = senha)