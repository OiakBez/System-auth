from flask import Flask, render_template, request, jsonify
from database import init_db, add_user

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

    try:
    
        user_id = add_user(name, email, password)

        return jsonify({
            "success": True,
            "message": "Usuário criado com sucesso.",
            "user_id": user_id
        }), 201

    except Exception as error:
        print(error)

        return jsonify({
            "success": False,
            "message": "Não foi possível criar o usuário."
        }), 500



if __name__ == "__main__":
    app.run(debug=False)