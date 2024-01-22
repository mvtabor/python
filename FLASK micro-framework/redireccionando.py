from flask import Flask, request, url_for, redirect
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
    return redirect(url_for('fungi', post_id=2)) #5
    return 'libros'

#5 redireccionamiento; siempre hay que utilizar el return
