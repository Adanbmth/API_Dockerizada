from database.db import get_connection
from .entities.especialidad import Especialidad

class EspecialidadModel():
    @classmethod
    def get_especialidades(self):
        try:
            connection=get_connection()
            especialidades=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT claveespecialidad, nombreespecialidad, creditos, clavecarrera from especialidad")
                resultset=cursor.fetchall()

                for row in resultset:
                    especialidad = Especialidad(row[0],row[1],row[2],row[3])
                    especialidades.append(especialidad.to_JSON())
            connection.close()
            return especialidades
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def get_especialidad(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT claveespecialidad, nombreespecialidad, creditos, clavecarrera from especialidad WHERE claveespecialidad = %s", (id,))
                row = cursor.fetchone()

                especialidad = None
                if row != None:
                    especialidad = Especialidad(row[0], row[1], row[2], row[3])
                    especialidad = especialidad.to_JSON()

            connection.close()
            return especialidad
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def add_especialidad(self, especialidad):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO especialidad (claveespecialidad, nombreespecialidad, creditos, clavecarrera) 
                                VALUES (%s, %s, %s, %s)""", (especialidad.claveespecialidad, especialidad.nombreespecialidad, especialidad.creditos, especialidad.clavecarrera))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex) 
        
    
    @classmethod
    def update_especialidad(self, especialidad):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE especialidad SET nombreespecialidad = %s, creditos = %s, clavecarrera = %s 
                                WHERE claveespecialidad = %s""", (especialidad.nombreespecialidad, especialidad.creditos, especialidad.clavecarrera, especialidad.claveespecialidad))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_especialidad(self, especialidad):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM especialidad WHERE claveespecialidad = %s", (especialidad.claveespecialidad,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)