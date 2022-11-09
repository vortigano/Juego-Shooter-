import mysql.connector
import string
from mysql.connector import Error


class AccesoDatos:
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='shooter_db')
        except Error as ex:
            print(f'Fallo: {ex}')
    
    def ejecutarAccion(self, string):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute(string)
                self.conexion.commit()
                print('guardadoOk')
            except Error as ex:
                print(f'Fallo: {ex}')

    def listarRanking(self):

        if self.conexion.is_connected():
            try:
                self.cursor=self.conexion.cursor()
                self.cursor.execute('select nombre, mejorPuntaje from historial order by mejorPuntaje desc limit 5;')
                self.respuesta=self.cursor.fetchall()

                #print(self.respuesta)        
                return str(self.respuesta)  #seguir desde acá
            except Error as ex:
                print(f'Fallo: {ex}')

    def buscarJugador(self):
        if self.conexion.is_connected():
            try:
                self.cursor=self.conexion.cursor()
                self.cursor.execute('select nombre, mejorPuntaje from historial order by mejorPuntaje desc limit 5;')
                self.respuesta=self.cursor.fetchall()


            except Error as ex:
                print(f'Fallo: {ex}')

############------Pruebas


#agregar="insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) value ('Jugador6',2,80,140);"
#modificar="UPDATE historial SET nombre = 'JugadorX' WHERE id=5;"
#eliminar="delete from historial where id=9;"
#acceso=AccesoDatos()
#acceso.ejecutarAccion(agregar)
