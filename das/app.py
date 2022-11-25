from pathlib import Path
from typing import List
import json

from flask import Flask, render_template, request
from flask_cors import CORS

from .outlook import Outlook
from .algorithms.triple_DES import triple_des_decrypt, triple_des_encrypt
from .algorithms import convert
from .key_manager import keys

HERE = Path(__file__).parent
ROOT = HERE.parent
STATIC = HERE / "static"

ENCRYPTED_MESSAGE_MARKER = "DAS ENCRYPTED MESSAGE"
KEY_REQUEST_MARKER = "DAS KEY REQUEST"
KEY_RESPONSE_MARKER = "DAS KEY RESPONSE"
DES_KEY_MARKER = "DAS DES KEY"

app = Flask(
    __name__,
)
CORS(app)

############### PAGES ###############
@app.route("/")
def index():
    """Render and return index.html"""
    return render_template("index.html")


def decrypt(email):
    email["body"] = email["body"].strip(ENCRYPTED_MESSAGE_MARKER)
    return  # TODO: delete this once key loading is complete
    k1, k2, k3 = keys.get_3des_key(email["sender"])
    ct = email["body"].strip(ENCRYPTED_MESSAGE_MARKER)
    ct_bin = convert.encode(ct)
    pt_bin = triple_des_decrypt(ct_bin, k1, k2, k3)
    pt = convert.decode(pt_bin)
    email["body"] = pt


def encrypt(email):
    email["body"] = ENCRYPTED_MESSAGE_MARKER + email["body"]
    return  # TODO: delete this once key loading is complete
    k1, k2, k3 = keys.get_3des_key(email["to"])
    pt = email["body"]
    pt_bin = convert.encode(pt)
    ct_bin = triple_des_encrypt(pt_bin, k1, k2, k3)
    ct = convert.decode(ct_bin)
    email["body"] = ENCRYPTED_MESSAGE_MARKER + ct


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
def get_folders(account: int) -> List[str]:
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
    res = []
    for e in MAIL.get_emails(folder):
        if e["body"].startswith(ENCRYPTED_MESSAGE_MARKER):
            decrypt(e)
            res.append(e)
        elif e["body"].startswith(
            KEY_REQUEST_MARKER
        ):  # Someone requested a secure key for future communication
            # Generate a key
            k = keys.generate_des_key()
            # Save it
            keys.save_3des_key(e["sender"], *k)

            # Encrypt the key
            user_pub = e["body"].strip(KEY_REQUEST_MARKER)
            pt = convert.decode(k)
            ct = convert.decode(k)  # TODO: encrypt this RSA.encrypt(pt, user_pub)

            # Send the key back to the requestor so that they can say what they want
            MAIL.send(e["sender"], e["subject"], KEY_RESPONSE_MARKER + ct)
        elif e["body"].startswith(KEY_RESPONSE_MARKER):
            # The sender has accepted a key request and responded with the DES key

            # Use my private RSA key to decrypt the DES key
            ct = e["body"].strip(KEY_RESPONSE_MARKER)
            my_pvt = keys.get_private_rsa_key(MAIL.account.Name)
            pt = ct  # TODO: decrypt this RSA.decrypt(ct, my_pvt)
            k = convert.encode(pt)

            # Save it
            keys.save_3des_key(e["sender"], *k)

            e["body"] = "SECURE LOC ESTABLISHED"
            res.append(e)

    return res[page * 20 : (page + 1) * 20]


@app.post("/api/send/<from_account>")
def send_email(from_account: int):
    email = json.loads(request.data)
    try:
        return send(from_account, email)
    except:
        return request_key(from_account, email["to"])


def send(from_account, email):
    MAIL = Outlook()
    MAIL.select_account(int(from_account))
    encrypt(email)
    MAIL.send(email["to"], email["subject"], email["body"])
    return "200"

def request_key(from_account, user):
    MAIL = Outlook()
    MAIL.select_account(int(from_account))
    MAIL.send(
        user,
        "DAS Request",
        KEY_REQUEST_MARKER #+ keys.get_public_rsa_key(),
    )
    return "300"


if __name__ == "__main__":
    app.run()
