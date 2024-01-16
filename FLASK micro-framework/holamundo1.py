from flask import Flask
app = Flask(__name__) #1

@app.route('/') #2

def index():
    return 'Hello, world'

@app.route('/fungi')

def fungi():
    return 'fungi'

@app.route('/milton')
def milton():
    return 'milton'

@app.route('/libros')
def libros():
    return 'libros'


#PARA COMANDOS EN GITBASH

# py -3 -m venv venv ; esto, donde almacenamos el proyecto. lo que hará será crear una carpeta dentro de nuestro proyecto
#llamada venv.
# . venv/Scripts/activate ; activamos los ambientes virtuales con este comando. notar el punto


#1 esta variable tendrá el valor de main cuando ejecutemos este archivo.
#2 comenzamos a utilizar decoradores con @app.