import mysql.connector

midb = mysql.connector.connect(
    host="localhost",            
    user="root",
    password="saudade94",
    database="prueba"
)

cursor = midb.cursor()

#LISTAR DATOS
cursor.execute('select * from usuario') 
resultado = cursor.fetchall()
#resultado = cursor.fetchone()
print(resultado)


#cursor.execute('select * from usuario limit 1') #podemos limitar cierto set de datos, usando la palabra reservada de limit, seguido del número de elementos a los que queremos limitar#
#resultado = cursor.fetchall()
#print(resultado)


#VER DIFINICIONES DE TABLAS
#cursor.execute('show create table usuario') #2

#INSERTAR DATOS
#sql = 'insert into usuario (email, username, edad) values (%s, %s, %s)' #1
#values = ('winter@correo.ca', 'northY', 30)

#ACTUALIZA DATOS
#sql = 'update usuario set email = %s where id = %s'#5
#values = ('fall@correo.com', 6)
#cursor.execute(sql, values) #3

#midb.commit() #4

#print(cursor.rowcount)

#1: escribimos la consulta que queremos ejecutar y en el paréntesis indicamos lo datos que queremos ingresar.
#seguido, indicamos los valores a ingresar.
#2 : con esta instrucción podemos ver lo que contenía el módelo.
#3: al ejecutar una consulta teniendo valores que pueden ser reemplazados, .execute() recibirá dos argumentos: 
  #a) la consulta sql; b) los valores a ingresar.
#4: este método hará que se guarden los datos, tomando los datos y ejecutando la consulta sql directamente en la base de datos.

#5: actualizamos datos



#sql = 'delete from usuario where id = %s'
#values = (6, ) #mediante una tupla indicamos el valor que queremos eliminar, usamos una coma -,- y el elemento por el que vamos a reemplazar -un espacio vacio-.
#cursor.execute(sql, values)
#midb.commit()