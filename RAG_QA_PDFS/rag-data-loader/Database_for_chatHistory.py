import psycopg2
from psycopg2 import sql

# Conecta a PostgreSQL (a la base de datos 'postgres' por defecto)
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Mascota3",
    dbname="postgres"
)

connection.autocommit = True  # Habilita el autocommit para ejecutar comandos como CREATE DATABASE

# Crea un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Crea la base de datos 'database164'
cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('pdf_rag_history')))
print("Base de datos 'pdf_rag_history' creada con éxito")

# Cierra la conexión a la base de datos 'postgres'
cursor.close()
connection.close()
