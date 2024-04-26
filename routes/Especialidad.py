from flask import Blueprint, jsonify, request

#Models
from models.especialidadModel import EspecialidadModel

# Entities
from models.entities.especialidad import Especialidad

main = Blueprint('especialidad_blueprint',__name__)

@main.route('/')
def get_especialidades():
    try:
        especialidad = EspecialidadModel.get_especialidades()
        return jsonify(especialidad)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_especialidad(id):
    try:
        especialidad = EspecialidadModel.get_especialidad(id)
        if especialidad != None:
            return jsonify(especialidad)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_especialidad():
    try:
        clave = request.json['Clave']
        nombre = request.json['Especialidad']
        creditos = int(request.json['Creditos'])
        carrera = request.json['Carrera']
        especialidad = Especialidad(clave, nombre, creditos, carrera)

        affected_rows = EspecialidadModel.add_especialidad(especialidad)

        if affected_rows == 1:
            return jsonify(especialidad.claveespecialidad)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_especialidad(id):
    try:
        nombre = request.json['Especialidad']
        creditos = int(request.json['Creditos'])
        carrera = request.json['Carrera']
        especialidad = Especialidad(id, nombre, creditos, carrera)

        affected_rows = EspecialidadModel.update_especialidad(especialidad)

        if affected_rows == 1:
            return jsonify(especialidad.claveespecialidad)
        else:
            return jsonify({'message': "No especialidad updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_especialidad(id):
    try:
        especialidad = Especialidad(id)

        affected_rows = EspecialidadModel.delete_especialidad(especialidad)

        if affected_rows == 1:
            return jsonify(especialidad.claveespecialidad)
        else:
            return jsonify({'message': "No especialidad deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500