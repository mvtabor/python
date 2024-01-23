from flask import Flask, request, url_for, redirect, abort, render_template
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

app.route('/libros', methods=['POST', 'GET'])
def libros():
    #return render_template('libros.html') #6
     return {  #7 
       "username": 'mvtabor',
       "email": 'librero@viejo.com'
     }

#6 una vez importado de flask, render_templete, dentro le indicamos la ruta de la plantilla html -previamente creara dentro de la carpeta "template"-,
#que queremos renderizar.
#7 si queremos devolver objetos con JSON, simplemente colocamos un diccionario e indicamos las propiedades deseadas.
