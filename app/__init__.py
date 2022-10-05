from flask import Flask

app = Flask(__name__) 
app.secret_key = 'test2022'

from app.controllers import routes