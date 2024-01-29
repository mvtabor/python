rom flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saudade94",
    database="prueba"
)

cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'Hello, world'

@app.route('/post/<post_id>', methods=['POST', 'PUT', 'PATCH', 'DELETE'])
def fungi(post_id):
    if request.method == 'GET':
        return 'El id del post es:' + post_id
    else:
        return 'Este es otro método y no GET'
@app.route('/post/<post_id>', methods=['GET']) 
def milton(post_id):
    return 'El id del post es:' + post_id

@app.route('/libros', methods=['POST', 'GET'])
def libros():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    return render_template('libros.html', usuarios=usuarios)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST": #mediante el objeto de request, verificaremos si el método que estamos llamando es el depósito.
        username=request.form['username']
        email=request.form['email'] #obtenemos los atributos del formulario
        edad=request.form['edad']
        sql='insert into Usuario (username, email, edad) values (%s, %s, %s)' #consulta sql a ejecutar; utilizando la sintaxis (%s), separamos en dos variables
        values = (username, email, edad)  #así evitamos que el usuario ingrese consultas sql dentro de los formularios.
        cursor.execute(sql, values)
        midb.commit()

        return redirect(url_for('libros'))
    return render_template('crear.html')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')
