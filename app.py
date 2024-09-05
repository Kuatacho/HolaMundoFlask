from flask import Flask, render_template
import psycopg2

app = Flask(__name__, template_folder='templates')

# Configuración de la base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:8157@localhost:5432/BdEjemploFlask"

@app.route('/')
def home():
    # Conectarse a la base de datos PostgreSQL
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Ejecutar la consulta SQL
    cursor.execute('SELECT * FROM users')
    myresults = cursor.fetchall()

    # Convertir los datos a un diccionario
    insertObject = []
    columnNames = [desc[0] for desc in cursor.description]
    for record in myresults:
        insertObject.append(dict(zip(columnNames, record)))

    # Cerrar la conexión
    cursor.close()
    conn.close()

    # Renderizar la plantilla con los datos obtenidos
    return render_template('index.html', data=insertObject)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
