from database.db import get_connection
from .entities.materia import Materia


class MateriaModel():
    @classmethod
    def get_materias(self):
        try:
            connection=get_connection()
            materias=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT clavemateria, nombremateria, creditos, semestre, clavecarrera from materia")
                resultset=cursor.fetchall()

                for row in resultset:
                    materia = Materia(row[0],row[1],row[2],row[3],row[4])
                    materias.append(materia.to_JSON())
            connection.close()
            return materias
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def get_materia(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT clavemateria, nombremateria, creditos, semestre, clavecarrera from materia WHERE clavemateria = %s", (id,))
                row = cursor.fetchone()

                materia = None
                if row != None:
                    materia = Materia(row[0], row[1], row[2], row[3], row[4])
                    materia = materia.to_JSON()

            connection.close()
            return materia
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def add_materia(self, materia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO materia (clavemateria, nombremateria, creditos, semestre, clavecarrera) 
                                VALUES (%s, %s, %s, %s, %s)""", (materia.clavemateria, materia.nombremateria, materia.creditos, materia.semestre, materia.clavecarrera))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex) 
        
    
    @classmethod
    def update_materia(self, materia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE materia SET nombremateria = %s, creditos = %s, semestre = %s, clavecarrera = %s 
                                WHERE clavemateria = %s""", (materia.nombremateria, materia.creditos, materia.semestre, materia.clavecarrera, materia.clavemateria))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_materia(self, materia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM materia WHERE clavemateria = %s", (materia.clavemateria,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)