import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

from email.message import EmailMessage
from werkzeug.security import check_password_hash
from flask import Flask, render_template, request, jsonify, url_for
from database import (
    init_db, 
    add_user, 
    get_user_by_verification_token, 
    verify_user,
    get_user_by_email
    )

app = Flask(__name__)

init_db()

def send_verification_email(email, name, token):

    verification_link = url_for(
        "verify_email",
        token = token,
        _external=True
    )

    message = EmailMessage()

    message["Subject"] = "Confirme seu email - System Auth"
    message["From"] = os.getenv("MAIL_USERNAME")
    message["To"] = email

    message.set_content(
        f"""
Olá, {name}!

Obrigado por criar sua conta no System Auth.

Para confirmar seu e-mail, acesse:

{verification_link}

Se você não criou esta conta, ignore a mensagem.
"""
    )

    with smtplib.SMTP(
        os.getenv("MAIL_SERVER"),
        int(os.getenv("MAIL_PORT"))
    ) as server:

        server.starttls()

        server.login(
            os.getenv("MAIL_USERNAME"),
            os.getenv("MAIL_PASSWORD")
        )

        server.send_message(message)

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

    existing_user = get_user_by_email(email)

    if existing_user is not None:
        return jsonify({
            "success": False,
            "message": "Este e-mail já está cadastrado."
        }), 409

    try:
    
        user_id, verification_token = add_user(name, email, password)

        send_verification_email(email, name, verification_token)

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


@app.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not email or not password:

        return jsonify({
            "success": False,
            "message": "Preencha todos os campos."
        }), 400

    user = get_user_by_email(email)

    if user is None:

        return jsonify({
            "success": False,
            "message": "E-mail ou senha incorretos."
        }), 401

    if not check_password_hash(user["password"], password):

        return jsonify({
        "success": False,
        "message": "E-mail ou senha incorretos."
        }), 401

    return jsonify({
        "success": True,
        "message": "Login, realizado com sucesso!"
    }), 200

if __name__ == "__main__":
    app.run(debug=False)