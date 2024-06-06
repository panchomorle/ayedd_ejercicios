"""
Ejemplo de uso de SQL con Python

Basado en la BD de
https://github.com/lerocha/chinook-database/tree/master
"""

#1) importar el driver del SGBD
import sqlite3

#2) abrir la conexion
conection = sqlite3.connect("EjercicioBDD/Chinook_Sqlite.sqlite")

#3) OPCIONAL: setear para que el resultado de una query sea un dict y no una tupla
conection.row_factory = sqlite3.Row

#4) enviar la query por medio de la conexión abierta
#conection.execute("INSERT INTO Artist (ArtistId, Name) VALUES (300, 'Pancho Morlé')")
#conection.commit()

res = conection.execute("SELECT * FROM Artist")

#5) recorrer los resultados de la query
for row in res:
    #print(str(row['ArtistId']) + ' - ' + row['Name'])
    print(dict(row))
    
#6) cerrar la conexión (liberar recursos del SGBD, del SO y Red)
conection.close()

