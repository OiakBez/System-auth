# System Auth

Sistema de cadastro e autenticação desenvolvido com **Python, Flask e JavaScript**, criado com o objetivo de estudar conceitos fundamentais de autenticação, validação de dados, APIs e comunicação entre frontend e backend.

## 📌 Sobre o projeto

O **System Auth** é uma aplicação web simples que permite o cadastro de usuários e login através de uma API desenvolvida em Flask.

Durante o cadastro, os dados são validados tanto no frontend quanto no backend. As senhas são armazenadas de forma segura utilizando hash, e o usuário recebe um e-mail com um link para confirmação da conta.

O projeto foi desenvolvido principalmente como projeto de estudo para praticar a integração entre **Python e JavaScript**.

## Funcionalidades

- Cadastro de usuários
- Validação de dados no frontend
- Validação de dados no backend
- Validação de e-mail
- Verificação de senha
- Hash de senhas
- Login através de API
- Verificação de e-mail através de token
- Envio de e-mail utilizando SMTP
- Prevenção de cadastro com e-mail duplicado
- Comunicação entre JavaScript e Flask utilizando JSON
- Banco de dados SQLite
- Variáveis de ambiente com `.env`

## 🛠️ Tecnologias utilizadas

### Backend

- Python
- Flask
- SQLite
- Werkzeug
- python-dotenv
- SMTP

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- JSON

## 📂 Estrutura do projeto

```text
System-auth/
│
├── app.py
├── database.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── cadastro.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        ├── login.js
        └── cadastro.js
