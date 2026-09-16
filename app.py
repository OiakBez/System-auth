from flask import Flask, render_template, request, jsonify
from database import init_db

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/api/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "Preencha todos os campos."
        }), 400

    return jsonify({
        "success": True,
        "message": "Cadastro recebido pelo servidor!"
    })



if __name__ == "__main__":
    app.run(debug=False)