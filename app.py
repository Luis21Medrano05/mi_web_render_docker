from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

app = Flask(__name__)
app.secret_key = "tu_clave_secreta"  # Cambia esto por una clave segura

# Configuración de la base de datos (usaremos SQLite para la demostración)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)

# Crear las tablas (esto se ejecuta al arrancar la app si no existen)
with app.app_context():
    db.create_all()

# Ruta para la página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id  # Guardamos el id del usuario en la sesión
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Credenciales inválidas", "danger")
    return render_template('login.html')

# Ruta protegida: solo accesible si se ha iniciado sesión
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Debes iniciar sesión", "warning")
        return redirect(url_for('login'))
    return "Bienvenido al panel de control!"

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Has cerrado sesión", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
