from flask import Flask, request, url_for, redirect, abort, render_template
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
