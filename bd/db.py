import mysql.connector

midb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "pruebaPython")

cursor = midb.cursor()

cursor.execute('select * from Usuario')

#cursor = mysql.execute('show create table Usuario')

resultado = cursor.fetchall()

# resultado = cursor.fetchone()

#Inserta
sql = 'insert into Usuario (username, nombre, email) values (%s, %s, %s)'
values = ('micorreo', 'correo', 'micorreo@micorreo.com')
cursor.execute(sql, values)
midb.commit()

#Acutaliza
sql = 'update Usuario set email = %s where id = %s'
values = ('micorreo@micorreo.net', 4)
cursor.execute(sql, values)
midb.commit

cursor.execute('select * from Usuario')
resultado = cursor.fetchall()

#Elimina
sql  = 'delete from Usuario where id = %s'
values = (1, ) #Se necesita la coma para indicar que es tupla
cursor.execute(sql, values)
midb.commit

cursor.execute('select * from Usuario')
resultado = cursor.fetchall()

print(resultado)