from database.db import get_connection
from .entities.especial import Especial

class EspecialModel():
    @classmethod
    def get_especiales(self):
        try:
            connection=get_connection()
            especiales=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT claveespecial, nombremateria, creditos, semestre, claveespecialidad from materiaespecial")
                resultset=cursor.fetchall()

                for row in resultset:
                    especial = Especial(row[0],row[1],row[2],row[3],row[4])
                    especiales.append(especial.to_JSON())
            connection.close()
            return especiales
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def get_especial(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT claveespecial, nombremateria, creditos, semestre, claveespecialidad from materiaespecial WHERE claveespecial = %s", (id,))
                row = cursor.fetchone()

                especial = None
                if row != None:
                    especial = Especial(row[0], row[1], row[2], row[3], row[4])
                    especial = especial.to_JSON()

            connection.close()
            return especial
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def add_especial(self, especial):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO materiaespecial (claveespecial, nombremateria, creditos, semestre, claveespecialidad) 
                                VALUES (%s, %s, %s, %s, %s)""", (especial.claveespecial, especial.nombremateria, especial.creditos, especial.semestre, especial.claveespecialidad))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex) 
        
    
    @classmethod
    def update_especial(self, especial):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE materiaespecial SET nombremateria = %s, creditos = %s, semestre = %s, claveespecialidad = %s 
                                WHERE claveespecial = %s""", (especial.nombremateria, especial.creditos, especial.semestre, especial.claveespecialidad, especial.claveespecial))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_especial(self, especial):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM materiaespecial WHERE claveespecial = %s", (especial.claveespecial,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)