from pathlib import Path
from typing import List
import json

from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS

from .outlook import Outlook

import csv
import os

HERE = Path(__file__).parent
ROOT = HERE.parent
STATIC = HERE / "static"

ENCRYPTED_MESSAGE_MARKER = "DAS ENCRYPTED MESSAGE"
KEY_REQUEST_MARKER = "DAS KEY REQUEST"

app = Flask(
    __name__,
)
CORS(app)


def save_keys(rsa_pubkey, rsa_prikey, des_key_1, des_key_2, des_key_3, sender_name):
    keys = []
    field_names = [
        "User",
        "RSA Public Key",
        "RSA Private Key",
        "DES Key 1",
        "DES Key 2",
        "DES Key 3",
    ]
    current_keys = csv.reader("keys.csv", "rw")
    for rows in current_keys[1:]:
        keys.append(
            {
                "User": rows[0],
                "RSA Public Key": rows[1],
                "RSA Private Key": rows[2],
                "DES Key 1": rows[3],
                "DES Key 2": rows[4],
                "DES Key 3": rows[4],
            }
        )

    os.remove("keys.csv")

    keys.append(
        {
            "User": sender_name,
            "RSA Public Key": rsa_pubkey,
            "RSA Private Key": rsa_prikey,
            "DES Key 1": des_key_1,
            "DES Key 2": des_key_2,
            "DES Key 3": des_key_3,
        }
    )

    with open("keys.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(keys)


############### PAGES ###############
@app.route("/")
def index():
    """Render and return index.html"""
    return render_template("index.html")

def decrypt(email):
    email["body"] = email["body"].strip(ENCRYPTED_MESSAGE_MARKER)

def encrypt(email):
    email["body"] = ENCRYPTED_MESSAGE_MARKER + email["body"]


############### EMAIL ACTIONS ###############
@app.get("/api/getaccounts")
def get_accounts() -> List[tuple]:
    """
    Returns a list accounts currently accessible through outlook.
    E.g. [
        ("john.doe@mail.com", 0),
        ("jane.doe@mail.com", 1),
    ]
    The integer is what is provided to other api calls, e.g. "/api/getfolder/0/Inbox"
    """
    MAIL = (
        Outlook()
    )  # need to initialize this on every request due to some threading issues
    return MAIL.accounts

@app.get("/api/getfolders/<account>")
def get_folders(account:int) -> List[str]:
    """
    Returns a list folders available to the account.
    E.g. [
        "Inbox",
        "Sent",
        ...
    ]
    """
    MAIL = Outlook()
    MAIL.select_account(int(account))
    return list(MAIL.folders.keys())

@app.get("/api/getfolder/<account>/<folder>")
def getfolder(account: int, folder: str) -> List[dict]:
    """returns a list of dictionaries representing the contents of an outlook folder"""
    page = int(request.args.get("page", 0))
    MAIL = Outlook()
    MAIL.select_account(int(account))
    res = [
        e
        for e in MAIL.get_emails(folder)
        if e["body"].startswith(ENCRYPTED_MESSAGE_MARKER)
    ]
    for e in res:
        decrypt(e)
    return res[page * 20 : (page + 1) * 20]
    # return [decrypt(e) for e in res[page * 20 : (page + 1) * 20]]


@app.post("/api/send/<from_account>")
def send(from_account:int):
    """returns a list of dictionaries representing the contents of an outlook folder"""
    MAIL = Outlook()
    MAIL.select_account(int(from_account))
    data = json.loads(request.data)
    encrypt(data)  # This should determine the key based off of the "to" parameter and encrypt the "body"
    MAIL.send(data["to"], data["subject"], data["body"])
    return "200"


if __name__ == "__main__":
    app.run()
