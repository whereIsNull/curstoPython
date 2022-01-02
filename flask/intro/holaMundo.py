# En terminal:
# python3 -m venv venv
# . venv/bin/activate
# pip3 install Flask
# export FLASK_APP=holaMundo.py
# sudo apt install python3-flask
# flask run

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

# export FLASK_ENV=development indica que el entorno es desarrollo y así coge los cambios en caliente
@app.route('/post/<post_id>', methods = ['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post ' + post_id
    else :
        return 'El otro id ' + post_id

@app.route('/lele')
def lele():
    return 'lele'