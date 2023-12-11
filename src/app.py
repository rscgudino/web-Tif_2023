from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify, render_template, json

from flask_cors import CORS
import mysql.connector

app = Flask(__name__, static_url_path='/static')
CORS(app)

# Configuración de la base de datos (ajusta según tu configuración)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Sofi_2019',
    'database': 'obelisco',
    'auth_plugin': 'mysql_native_password'
}

# Función para establecer la conexión con la base de datos
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    print("Conexión a la base de datos establecida")
    return connection

# Ruta para el registro de usuarios
@app.route('/api/usuarios', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    print(f"Recibiendo datos: {data}")

    nombre = data.get('nombre')
    apellido = data.get('apellido')
    telefono = data.get('telefono')
    email = data.get('email')
    tipo_registro = data.get('tipo_registro')
    tipo_propiedad = data.get('tipo_propiedad')

    if nombre and apellido and email:
        try:
            with get_db_connection() as connection, connection.cursor() as cursor:
                query = "INSERT INTO usuarios (nombre, apellido, telefono, email, tipo_registro, tipo_propiedad) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (nombre, apellido, telefono, email, tipo_registro, tipo_propiedad)

                cursor.execute(query, values)
                connection.commit()

                print("Registro exitoso")
                return jsonify({'mensaje': 'Registro exitoso. Pronto nos comunicaremos contigo.'})

        except mysql.connector.Error as e:
            error_message = f"Error en la base de datos: {e}"
            print(error_message)
            return jsonify({'error': error_message})

    return jsonify({'error': 'Datos incompletos'})
# Nueva ruta para la vista de propiedad
@app.route('/propiedad/<int:propiedad_id>')
def propiedad(propiedad_id):
    # Lógica para recuperar los detalles de la propiedad con el ID proporcionado
    # Puedes usar la variable propiedad_id en tu consulta para recuperar la propiedad específica
    # Luego renderiza el template correspondiente, por ejemplo, propiedad.html
    return render_template('propiedades/propiedad.html', propiedad_id=propiedad_id)

    return jsonify({'mensaje': 'Registro exitoso'})


# Rutas para renderizar las páginas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alquiler')
def alquiler():
    return render_template('alquiler.html')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/proyecto')
def proyectos():
    return render_template('proyectos.html')

@app.route('/venta')
def ventas():
    return render_template('ventas.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

# Manejador de errores
@app.errorhandler(Exception)
def handle_error(e):
    return str(e), 500

if __name__ == '__main__':
    print("La aplicación Flask se está ejecutando.")
    app.run(debug=True)
