from flask import Flask, render_template
from database import init_db

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=False)