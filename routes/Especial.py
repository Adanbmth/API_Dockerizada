from flask import Blueprint, jsonify, request

#Models
from models.especialModel import EspecialModel

# Entities
from models.entities.especial import Especial

main = Blueprint('matesp_blueprint',__name__)

@main.route('/')
def get_especiales():
    try:
        especial = EspecialModel.get_especiales()
        return jsonify(especial)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_especial(id):
    try:
        especial = EspecialModel.get_especial(id)
        if especial != None:
            return jsonify(especial)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_especial():
    try:
        clave = request.json['Clave']
        nombre = request.json['Materia']
        creditos = int(request.json['Creditos'])
        semestre = int(request.json['Semestre'])
        especialidad = request.json['Especialidad']
        especial = Especial(clave, nombre, creditos, semestre, especialidad)

        affected_rows = EspecialModel.add_especial(especial)

        if affected_rows == 1:
            return jsonify(especial.claveespecial)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_especial(id):
    try:
        nombre = request.json['Materia']
        creditos = int(request.json['Creditos'])
        semestre = int(request.json['Semestre'])
        especialidad = request.json['Especialidad']
        especial = Especial(id, nombre, creditos, semestre, especialidad)

        affected_rows = EspecialModel.update_especial(especial)

        if affected_rows == 1:
            return jsonify(especial.claveespecial)
        else:
            return jsonify({'message': "No materia updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_especialidad(id):
    try:
        especial = Especial(id)

        affected_rows = EspecialModel.delete_especial(especial)

        if affected_rows == 1:
            return jsonify(especial.claveespecial)
        else:
            return jsonify({'message': "No materia deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500