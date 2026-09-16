from flask import Flask, render_template, request, jsonify
from database import (
    init_db, 
    add_user, 
    get_user_by_verification_token, 
    verify_user
    )

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
    
        user_id, verification_token = add_user(name, email, password)

        print("TOKEN DE VERIFICAÇÃO:", verification_token)

        return jsonify({
            "success": True,
            "message": "Usuário criado com sucesso. Verifique seu email.",
            "user_id": user_id
        }), 201

    except Exception as error:
        print(error)

        return jsonify({
            "success": False,
            "message": "Não foi possível criar o usuário."
        }), 500

@app.route("/verify/<token>")
def verify_email(token):

    user = get_user_by_verification_token(token)

    if user is None:
        return "Token inválido ou expirado.", 400

    verify_user(user["id"])

    return "E-mail verificado com sucesso!"


if __name__ == "__main__":
    app.run(debug=False)