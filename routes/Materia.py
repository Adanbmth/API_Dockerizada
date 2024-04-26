from flask import Blueprint, jsonify, request

#Models
from models.materiaModel import MateriaModel

# Entities
from models.entities.materia import Materia

main = Blueprint('materia_blueprint',__name__)

@main.route('/')
def get_materias():
    try:
        materia = MateriaModel.get_materias()
        return jsonify(materia)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_materia(id):
    try:
        materia = MateriaModel.get_materia(id)
        if materia != None:
            return jsonify(materia)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_materia():
    try:
        clave = request.json['Clave']
        nombre = request.json['Materia']
        creditos = int(request.json['Creditos'])
        semestre = int(request.json['Semestre'])
        carrera = request.json['Carrera']
        materia = Materia(clave, nombre, creditos, semestre, carrera)

        affected_rows = MateriaModel.add_materia(materia)

        if affected_rows == 1:
            return jsonify(materia.clavemateria)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_materia(id):
    try:
        nombre = request.json['Materia']
        creditos = int(request.json['Creditos'])
        semestre = int(request.json['Semestre'])
        carrera = request.json['Carrera']
        materia = Materia(id, nombre, creditos, semestre, carrera)

        affected_rows = MateriaModel.update_materia(materia)

        if affected_rows == 1:
            return jsonify(materia.clavemateria)
        else:
            return jsonify({'message': "No materia updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_materia(id):
    try:
        materia = Materia(id)

        affected_rows = MateriaModel.delete_materia(materia)

        if affected_rows == 1:
            return jsonify(materia.clavemateria)
        else:
            return jsonify({'message': "No materia deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500