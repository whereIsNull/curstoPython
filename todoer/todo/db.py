import mysql.connector

import click #Ejecutar comandos desde la terminal
from flask import current_app, g #variable de la aplicación (se usará para almacenar el usuario, supongo que es variable de sesión)
from flask.cli import with_appcontext #appcontext: variables en la configuración de la aplicación
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE_DB'],
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@click.command('init-db') #Desde el terminal ejecuto 'flask init-db' y ejecutará esta función
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()

def init_app(app):
    app.teardown_appcontext(close_db) #Ejecuta funciones como argumento una vez ejecutadas la función seleccionada: en este caso un endpoint
    app.cli.add_command(init_db_command)