from app.models.models import conexao
from flask import jsonify, render_template, request, redirect, url_for, session, send_file
from authlib.integrations.flask_client import OAuth
import json
import os
from app import app

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    client_id = '838897217727-2p26l7nh0lpqub2mktg0kbc7d0gsb8qo.apps.googleusercontent.com',
    client_secret = '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',
    server_metadata_url=CONF_URL,  
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@app.route('/')
@app.route('/index')
def index():
    user = session.get('user')
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login', methods=['POST' , 'GET'])
def login():
    # args no lugar no form aceita por metodo GET
    if request.method == 'POST':
        usuario = request.form.get('usuario').strip()
        senha = request.form.get('senha').strip()

        if usuario and senha:
            teste = conexao(host = 'us-cdbr-east-06.cleardb.net', 
                        user = 'b6ac0eeaf6adcc', 
                        password = '5d88e207', 
                        database='heroku_bf31a8a8a28ff60')

            if teste.consultar('login', ['email', 'senha'], [usuario, senha]):
                string = (teste.ver('login'))
                teste.sair()
                return render_template('login.html', user = usuario, password = senha, bd = string)

            else:
                return redirect('/index')
    
    if session['user']:
        return render_template('/login.html', user = session['user'])

    return redirect('/index')

@app.route('/ajuda')
def ajuda():
    user = session.get('user')
    return render_template('ajuda.html', user=user)

@app.route('/login_google')
def login_google():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorized', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorized')
def authorized():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/conta_nova')
def conta_nova():
    return render_template('conta_nova.html')

@app.route('/dowload')
def dowload():
    with open('api.json', 'w+', encoding='utf-8') as arquivo:
        teste = conexao(host = 'us-cdbr-east-06.cleardb.net', 
                    user = 'b6ac0eeaf6adcc', 
                    password = '5d88e207', 
                    database='heroku_bf31a8a8a28ff60')

        lista = dict(teste.ver('login'))
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)
        teste.sair() 

        wd = os.path.dirname(__file__)
        wd = wd.replace('\\app', '').replace('controllers', '')
        nome_arquivo = wd + f'{arquivo.name}'

        send_file(nome_arquivo, as_attachment=True)
    return redirect('/login')