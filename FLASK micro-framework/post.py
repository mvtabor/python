from flask import Flask
app = Flask(__name__) #1

@app.route('/') #2

def index():
    return 'Hello, world'

@app.route('/post/<post_id>') #podriamos obtener un entero utilizando int:, ejem 'int:post_id'
def fungi(post_id):
    return 'El id del post es:' + post_id
