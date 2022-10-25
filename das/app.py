from pathlib import Path
from typing import List

from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS

from .outlook import Outlook

HERE = Path(__file__).parent
ROOT = HERE.parent
STATIC = HERE / "static"


app = Flask(
    __name__,
)
CORS(app)

############### PAGES ###############
@app.route("/")
def index():
    """Render and return index.html"""
    return render_template("index.html")

@app.route("/main")
def main():
    """Render and return main.html"""
    return render_template("main.html", python_variable="Success")

@app.get("/api/<username>/inbox")
def get_inbox(username):
    return send_from_directory(STATIC, "mock/example_inbox.json")

@app.post("/api/encrypt/<path>")
def encrypt(path):
    return f"I don't know how to do this yet: {path}"


############### EMAIL ACTIONS ###############
@app.get("/api/getaccounts")
def get_accounts() -> List[dict]:
    """
    Returns a list accounts currently accessible through outlook.
    E.g. [
        ("john.doe@mail.com", 0),
        ("jane.doe@mail.com", 1),
    ]
    The integer is what is provided to other api calls, e.g. "/api/getfolder/0/Inbox"
    """
    MAIL = Outlook()  # need to initialize this on every request due to some threading issues
    return MAIL.accounts

@app.get("/api/getfolder/<account>/<folder>")
def getfolder(account:int, folder:str) -> List[dict]:
    """returns a list of dictionaries representing the contents of an outlook folder"""
    page = int(request.args.get("page", 0))
    MAIL = Outlook()
    MAIL.select_account(int(account))
    MAIL.load(folder)
    res = MAIL.get_emails(folder)
    return res[page*20:(page+1)*20]

@app.post("/api/send")
def send():
    """returns a list of dictionaries representing the contents of an outlook folder"""
    MAIL = Outlook()
    data = request.data
    MAIL.select_account(data["account"])
    MAIL.send(data["to"], data["subject"], data["body"])




if __name__ == "__main__":
    app.run( )