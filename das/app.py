from pathlib import Path

from flask import Flask, render_template,send_from_directory
from flask_cors import CORS

HERE = Path(__file__).parent
ROOT = HERE.parent
STATIC = HERE / "static"

app = Flask(
    __name__,
)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html", python_variable="Success")

@app.get("/api/<username>/inbox")
def get_inbox(username):
    return send_from_directory(STATIC, "mock/example_inbox.json")

@app.post("/api/encrypt/<path>")
def encrypt(path):
    return f"I don't know how to do this yet: {path}"


if __name__ == "__main__":
    app.run( )