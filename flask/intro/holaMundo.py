# En terminal:
# python3 -m venv venv
# . venv/bin/activate
# pip3 install Flask
# export FLASK_APP=holaMundo.py
# sudo apt install python3-flask
# flask run

from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pruebapython'
)

cursor = midb.cursor(dictionary = True)

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

@app.route('/lele', methods=['POST','GET'])
def lele():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    return render_template('lele.html', usuarios=usuarios)

@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')

@app.route('/crear', methods = ['GET', 'POST'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        sql = 'insert into usuario(username, email) values(%s, %s)'
        values = (username, email)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('lele'))
    return render_template('crear.html')

@app.route('/getJSON', methods = ['GET', 'POST'])
def getJSON():
    #print(url_for('index')) #Nombre de la función, en este caso equivaldría a la ruta '/'
    # print(url_for('lala', post_id = 2)) #Nombre de la función, en este caso equivaldría a la ruta '/lala' y el segundo argumento el parámetro de la función
    # print(request.form)
    # print(request.form['llave1'])
    #abort(401) #Envía error, parámetro: código http
    #return redirect(url_for('lala', post_id = 2)) #Para redireccionar es imprescindible hadcerlo en el return
    #return 'lele'
    
    # return render_template('lele.html') #flask busca la ruta 'templates/lele.html'

    return {
        'username': 'chanchito',
        'email': 'chanch@chanch.com'
    } #Devuelve un JSON