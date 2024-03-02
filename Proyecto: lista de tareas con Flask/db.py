import mysql.connector

import click #nos permité ejecutar comandos en la terminal, con la cual crearemos tablas y la relación entre ellas
from flask import current_app, g #current mantiene la app ejecutada y g es una variable a la cual le asignaremos valor
from flask.cli import with_appcontext #cuando ejecutamos los scrips podemos acceder a las variables de la config de nuestra app como el host, user y password
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']            
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

#definiremos una func que nos permitirá cerrar la conex de la db cada vez que realicemos una petición
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
def init_db():
    db,c = get_db()

    for i in instructions:
        c.execute(i)
    
    db.commit()

@click.command('init-db')
@with_appcontext

def init_db_command():
    init_db() #COMENTAR PAR QUE CORRA flask init-db EN LA CONSOLA
    click.echo('Base de datos inicializada')
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)