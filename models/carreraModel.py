from database.db import get_connection
from .entities.carrera import Carrera

class CarreraModel():

    @classmethod
    def get_carreras(self):
        try:
            connection=get_connection()
            carreras=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT clavecarrera, nombrecarrera, estructuragenetica from carrera")
                resultset=cursor.fetchall()

                for row in resultset:
                    carrera = Carrera(row[0],row[1],row[2])
                    carreras.append(carrera.to_JSON())
            connection.close()
            return carreras
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_carrera(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT clavecarrera, nombrecarrera, estructuragenetica from carrera WHERE clavecarrera = %s", (id,))
                row = cursor.fetchone()

                carrera = None
                if row != None:
                    carrera = Carrera(row[0], row[1], row[2], row[3])
                    carrera = carrera.to_JSON()

            connection.close()
            return carrera
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def add_carrera(self, carrera):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO carrera (clavecarrera, nombrecarrera, estructuragenetica) 
                                VALUES (%s, %s, %s)""", (carrera.clavecarrera, carrera.nombrecarrera, carrera.estructuragenetica))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def update_carrera(self, carrera):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE carrera SET nombrecarrera = %s, estructuragenetica = %s 
                                WHERE clavecarrera = %s""", (carrera.nombrecarrera, carrera.estructuragenetica,carrera.clavecarrera))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_carrera(self, carrera):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM carrera WHERE clavecarrera = %s", (carrera.clavecarrera,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)