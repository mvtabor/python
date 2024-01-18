from flask import Flask, request, url_for
app = Flask(__name__)

app.route('/')
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

@app.route('/libros', methods=['POST'])
def libros():
    print(url_for('fungi', post_id=2)) #4
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'libros'


#4 indicamos el nombre de la función, no la ruta, y como segundo argumento, el valor de post_id.
