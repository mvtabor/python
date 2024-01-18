from flask import Flask, request #1
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world'

@app.route('/libros', methods=['POST'])
def libros():
    print(request.form) #1
    print(request.form['llave1']) #2
    print(request.form['llave2'])
    return 'libros'

#1 haremos uso del objeto request para ver los datos enviados a través de un formulario.
#2 lo utilizamos para obtener los datos en un formulario


#EN OTRA VENTANA GITBASH
# curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/libros

# curl nos permite realizar llamadas a nuestro servicio. Le indicamos el tipo de método a utilizar. Podremos ver los datos que se están enviando a través de un 
#formulario, haciendo uso del objto "request".
