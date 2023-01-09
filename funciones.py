# Fichero de funciones

##Función para mostrar información tras la conexión.

def Mostrar_Pelicuas(db):
    sql= "select * from peliculas"
    cursor=db.cursor()
    cursor.execute(sql)
    datos = cursor.fetchall()
    return datos
