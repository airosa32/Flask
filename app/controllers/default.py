from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    nome = 'Tiago'
    dados = list(range(10))
    return render_template('index.html',nome = nome, contador = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
