from flask import Blueprint, jsonify, request

#Models
from models.carreraModel import CarreraModel

# Entities
from models.entities.carrera import Carrera

main = Blueprint('carrera_blueprint',__name__)

@main.route('/')
def get_carreras():
    try:
        carreras = CarreraModel.get_carreras()
        return jsonify(carreras)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/<id>')
def get_carrera(id):
    try:
        carrera = CarreraModel.get_carrera(id)
        if carrera != None:
            return jsonify(carrera)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_carrera():
    try:
        clave = request.json['Clave']
        nombre = request.json['Nombre']
        genetica = int(request.json['Estructura Genetica'])
        carrera = Carrera(clave, nombre, genetica)

        affected_rows = CarreraModel.add_carrera(carrera)

        if affected_rows == 1:
            return jsonify(carrera.clavecarrera)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_carrera(id):
    try:
        nombre = request.json['Nombre']
        genetica = int(request.json['Estructura Genetica'])
        carrera = Carrera(id, nombre, genetica)

        affected_rows = CarreraModel.update_carrera(carrera)

        if affected_rows == 1:
            return jsonify(carrera.clavecarrera)
        else:
            return jsonify({'message': "No carrera updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_carrera(id):
    try:
        carrera = Carrera(id)

        affected_rows = CarreraModel.delete_carrera(carrera)

        if affected_rows == 1:
            return jsonify(carrera.clavecarrera)
        else:
            return jsonify({'message': "No carrera deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500