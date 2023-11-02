import mysql.connector #1

midb = mysql.connector.connect( #2
    host="localhost",            
    user="root",
    password="saudade94",
    database="prueba"
)

cursor = midb.cursor() #3

cursor.execute('select * from usuario') #4

#5
resultado = cursor.fetchall() #6
#resultado = cursor.fetchone() #7 

print(resultado)

#1: esta librería nos permitirá conectarnos con mysql.
#2: al importar, nos deja disponible la varible mysql.connector y utilizamos el método connect
# #que recibe los 4 argumentos a continuación: (arriba).

#Este método devuelve una instancia de base de datos.

#3: el cursor nos permite interactuar con las base de datos mediante su lenguaje.
#4: con cursor llamamos al método de execute y le pasamos consultas en sql.
#5: creamos la variable resultado para obtener los resultados.
#6: .fetchall() #devolverá todas las instancias de los elementos encontradas y las asignará a la variable declarada.
#7: .fetchone() #devolverá el primer elemento encontrado en la base de datos.

