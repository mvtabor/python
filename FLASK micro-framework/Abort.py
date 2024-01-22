from flask import Flask, request, url_for, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world'

@app.route('/post/<post_id>', methods=['POST', 'PUT', 'PATCH', 'DELETE']) #podriamos obtener un entero utilizando int:, ejem 'int:post_id'
def fungi(post_id):
    if request.method == 'GET':
        return 'El id del post es:' + post_id
    else:
        return 'Este es otro método y no GET'

  @app.route('/post/<post_id>', methods=['GET']) #podriamos obtener un entero utilizando int:, ejem 'int:post_id'
def milton(post_id):
    return 'El id del post es:' + post_id

@app.route('/libros', methods=['POST', 'GET'])
def libros():
    abort(401) #6
    return redirect(url_for('fungi', post_id=2))
    return 'libros'

#6 importandolo, lo utilizaremos para detener la ejecución de nuestra función y devolver un mensaje (código).
