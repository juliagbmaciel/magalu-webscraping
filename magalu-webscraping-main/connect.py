import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='magazineluiza',
        user='root',
        password=''
    )
except:
    print("Erro ao conectar")