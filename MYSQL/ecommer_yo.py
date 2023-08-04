import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_imbachi_juan"
)
#print(type(db))


cursor=db.cursor()
cursor.execute('SHOW DATABASES')
#print(type(cursor))
for dbs in cursor:
     print(dbs)

# for n in cursor:
#     print(n)
print('----------TABLAS----------------')
cursor.execute("SHOW TABLES")
for n in cursor:
    print(n)

#print('---------------------------')

#cursor.execute ("""INSERT INTO marcas (nombre) VALUES ('MOTOROLA') """)
#db.commit()
#cursor.execute('select * from marcas')
#for ap in cursor:
     #print(ap[0])
     #print(ap[1])

#cursor.execute("DELETE FROM marcas WHERE id_marca= 5")
#db.commit()

#cursor.execute("UPDATE roles SET nombre_Usuario ='Eric Candro' WHERE id_rol=3")
#db.commit()

#cursor.execute("UPDATE roles SET nombre_Usuario ='ERIC CANDRO ' WHERE id_rol=3")
#db.commit()

#cursor.execute("""CREATE TABLE locales(
               #id_local INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
               #ubicacion VARCHAR(100) NOT  NULL
               #); """)

#db.commit()

#cursor.execute(""" INSERT INTO locales (ubicacion) VALUES ('SAN MATEO') """)
#db.commit()
print('-------------CATEGORIAS---------------------')
cursor.execute('select * from categorias')
for ap in cursor:
    print(ap[0])
    print(ap[1])

print('----------LOCALES-------------')
cursor.execute('select * from locales')
for ap in cursor:
    print(ap[0])
    print(ap[1])

print('-----------MARCAS--------------')
cursor.execute('select * from marcas')
for ap in cursor:
    print(ap[0])
    print(ap[1])

print('----------PRODUCTOS------------')
cursor.execute('select * from productos')
for ap in cursor:
    print(ap[0])
    print(ap[1])
    print(ap[2])
    print(ap[3])
    print(ap[4])
    print(ap[5])
    print(ap[6])
    print(ap[7])
    print(ap[8])

print('-----------ROLES--------------')
cursor.execute('select * from roles')
for ap in cursor:
    print(ap[0])
    print(ap[1])
    print(ap[2])

print('----------USUARIOS------------')
cursor.execute('select * from usuarios')
for ap in cursor:
    print(ap[0])
    print(ap[1])
    print(ap[2])
    print(ap[3])
    print(ap[4])
    print(ap[5])

print('------------VENDEDORES----------')
cursor.execute('select * from vendedores')
for ap in cursor:
    print(ap[0])
    print(ap[1])














