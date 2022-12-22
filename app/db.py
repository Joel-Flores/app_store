#importando frameworks
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext

#importando instruciones para la base de datos
from app.schema import all_tables, values_tables

#funcion para llamar a la base de datos y al cursor
def get_db():
    if 'db' not in  g:
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary = True)
    return g.db, g.c

#funcion para cerrar la base de datos administrada por la app
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

#cargar tablas a la base de datos y datos basicos
def init_db():
    db, c = get_db()
    
    for instruction in all_tables:
        c.execute(instruction)
    db.commit()
    
    for instruction in values_tables:
        c.execute(instruction)
    db.commit()
    
#declarando nuevo comando para flask
@click.command(name = 'init-db')
@with_appcontext    
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

#funcion para que la app se encargue de las ejecuciones
def init_app(app):
        app.teardown_appcontext(close_db)
        app.cli.add_command(init_db_command)