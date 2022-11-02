import enum
from app.models.models import conexao
from flask import render_template, request, Response, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from app import app
import json

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
                teste.sair()
                session['user'] = usuario              
                return render_template('login.html', user = session['user'])
            else:
                return redirect('/index')
    
    try:
        if session['user']:              
            return render_template('login.html', user = session['user']) 
    except:  
        try:
            if session['user_google']:
                return render_template('login.html', user_google = session['user_google'])
        except:
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
    session['user_google'] = token['userinfo']
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user', None) or session.pop('user_google', None) 
    return redirect('/')

@app.route('/conta_nova', methods=['POST' , 'GET'])
def conta_nova():
    if request.method == 'POST':
        nome = request.form.get('nome').strip().split()
        usuario = request.form.get('usuario').strip()
        senha = str(request.form.get('senha').strip())
        
        if nome and usuario and senha:
            verificacao = 0

            for pos, letra in enumerate(usuario):
                if pos == len(senha):
                    porcentagem = (len(senha) - verificacao)*100/len(senha)
                    print(round(porcentagem))
                    print(usuario)
                    if round(porcentagem) < 40:
                        return render_template('conta_nova.html', not_valid = True)
                    
                    return render_template('index.html', new_acc = True)
                elif letra in senha:
                    print(letra)
                    verificacao += 1
                
    else:
        return render_template('conta_nova.html')

@app.route('/dowload')
def dowload():
    teste = conexao(host = 'us-cdbr-east-06.cleardb.net', 
                user = 'b6ac0eeaf6adcc', 
                password = '5d88e207', 
                database='heroku_bf31a8a8a28ff60')

    lista = dict(teste.ver('login'))
    lista_tratada = json.dumps(lista)

    teste.sair() 

    return Response(f'{lista_tratada}', mimetype='application/json',
            headers={'Content-Disposition':'attachment;filename=api.json'})