from email.policy import default
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    lista = list(range(10))
    return render_template('index.html', nome = 'tiago', lista = lista)

@app.route('/contato')
def contato():
    return render_template('contato.html')
