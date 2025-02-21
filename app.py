from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, esta es mi aplicación Flask con Docker en Render!"

if __name__ == "__main__":
    app.run(debug=True)
