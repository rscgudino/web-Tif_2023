from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos (ajusta según tu configuración)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Sofi_2019',
    'database': 'inmobiliaria'
}

# Función para establecer la conexión con la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Ruta para el registro de usuarios
@app.route('/api/usuarios', methods=['POST'])
def registrar_usuario():
    data = request.json

    nombre = data.get('nombre')
    apellido = data.get('apellido')
    telefono = data.get('telefono')
    email = data.get('email')
    tipo_registro = data.get('tipo_registro')
    tipo_propiedad = data.get('tipo_propiedad')

    if nombre and apellido and email:
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            # Ajusta la siguiente consulta según tu esquema de base de datos
            query = "INSERT INTO usuarios (nombre, apellido, telefono, email, tipo_registro, tipo_propiedad) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (nombre, apellido, telefono, email, tipo_registro, tipo_propiedad)

            cursor.execute(query, values)
            connection.commit()

            return jsonify({'mensaje': 'Registro exitoso'})

        except Exception as e:
            print(e)
            return jsonify({'error': 'Error en el registro'})

        finally:
            cursor.close()
            connection.close()

    return jsonify({'error': 'Datos incompletos'})

if __name__ == '__main__':
    app.run(debug=True)
