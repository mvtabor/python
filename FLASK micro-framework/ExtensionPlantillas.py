from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__) #1

@app.route('/') #2
def index():
    return 'Hello, world'

@app.route('/post/<post_id>', methods=['POST', 'PUT', 'PATCH', 'DELETE']) #podriamos obtener un entero utilizando int:, ejem 'int:post_id'
def fungi(post_id):
    if request.method == 'GET': #3
        return 'El id del post es:' + post_id
    else:
        return 'Este es otro método y no GET'
@app.route('/post/<post_id>', methods=['GET']) #podriamos obtener un entero utilizando int:, ejem 'int:post_id'
def milton(post_id):
    return 'El id del post es:' + post_id

@app.route('/libros', methods=['POST', 'GET'])
def libros():
    #abort(401)
    #return redirect(url_for('fungi', post_id=2)) #5
    #print(url_for('fungi', post_id=2)) #4
    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    #return render_template('libros.html') #6
    return {
        "username": 'mvtabor',
        "email": 'librero@viejo'
    }
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')
