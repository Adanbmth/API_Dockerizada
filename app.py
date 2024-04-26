from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from config import config
from os import environ
from routes import Carrera, Materia, Especial, Especialidad

app=Flask(__name__)


##################################################################################
def page_not_found(error):
    return "<h1>Not found page</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(Carrera.main, url_prefix='/api/carrera')
    app.register_blueprint(Materia.main, url_prefix='/api/materia')
    app.register_blueprint(Especial.main, url_prefix='/api/especial')
    app.register_blueprint(Especialidad.main, url_prefix='/api/especialidad')
    app.run()
