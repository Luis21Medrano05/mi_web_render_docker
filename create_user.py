from app import app
from models import db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Define el usuario y la contraseña deseados
    username = "admin"       # Puedes cambiar "admin" por el usuario que prefieras
    password = "admin123"    # Cambia "admin123" por la contraseña que desees

    # Crea el hash de la contraseña para almacenarla de forma segura
    password_hash = generate_password_hash(password, method="sha256")

    # Crea un nuevo usuario
    new_user = User(username=username, password_hash=password_hash)

    # Agrega y guarda el usuario en la base de datos
    db.session.add(new_user)
    db.session.commit()

    print("Usuario creado exitosamente.")
