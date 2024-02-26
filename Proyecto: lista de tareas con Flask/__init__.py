import os #esta librería o módulo nos permite acceder a ciertas cosas del sistema operativo, como las variables de entorno

from flask import Flask

def create_app(): #nos servirá cuando queramos hacer testing o crear varias instancias de nuestra app
    app = Flask(__name__) #definimos nuestra constante, mediante el constructor de Flask;todas las app de Flask son una instancia de la clase Flask

    app.config.from_mapping(
        SECRET_KEY='mikey', #llave para definir las sesiones
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )  #configuramos nuestra app utilizando las variables de entorno
                               #.from_mapping() nos va a permitir variables de configuración
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    @app.route('/hola')
    def hola():
        return 'Tacos de cabeza'

    return app
