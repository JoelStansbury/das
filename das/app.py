from pathlib import Path
from typing import List
import json

from flask import Flask, render_template, request
from flask_cors import CORS

from .outlook import Outlook
from .algorithms.triple_DES import triple_des_decrypt, triple_des_encrypt
from .algorithms.RSA import RSA
from .algorithms import convert
from .key_manager import keys

HERE = Path(__file__).parent
ROOT = HERE.parent
STATIC = HERE / "static"

ENCRYPTED_MESSAGE_MARKER = "DAS ENCRYPTED MESSAGE"
KEY_REQUEST_MARKER = "DAS KEY REQUEST"
KEY_RESPONSE_MARKER = "DAS KEY RESPONSE"
DES_KEY_MARKER = "DAS DES KEY"

app = Flask(__name__)
CORS(app)

############### PAGES ###############
@app.route("/")
def index():
    """Render and return index.html"""
    return render_template("index.html")


def decrypt(email):
    # email["body"] = email["body"].strip(ENCRYPTED_MESSAGE_MARKER)
    # return  # TODO: delete this once key loading is complete
    try:
        k1, k2, k3 = keys.get_3des_key(email["sender"]["email"])
        ct = email["body"].strip(ENCRYPTED_MESSAGE_MARKER)
        ct_bin = convert.encode(ct)
        pt_bin = [triple_des_decrypt(b, k1, k2, k3) for b in ct_bin]
        pt = convert.decode(pt_bin)
        email["body"] = pt
    except:
        email["body"] += "\n\n COULD NOT FIND KEY"


def encrypt(email):
    k1, k2, k3 = keys.get_3des_key(email["to"])
    pt = email["body"]
    pt_bin = convert.encode(pt)
    ct_bin = [triple_des_encrypt(b, k1, k2, k3) for b in pt_bin]
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
    # need to initialize this on every request due to some threading issues
    MAIL = Outlook()
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
            _key = keys.get_3des_key(e["sender"]["email"])
            if _key is None or not all(_key):
                print(f"Making a key for {e['sender']['email']}")
                # Extract the public key
                n, k = [int(x) for x in e["body"].strip(KEY_REQUEST_MARKER).strip()[1:-1].split()]
                rsa = RSA(3,7)
                rsa.n = n
                rsa.k = k
                # Generate a key
                encrypted_des_key = " ".join([
                    str(rsa.encrypt(int(x,2)))
                    for x in keys.generate_des_key(e["sender"]['email'])
                ])
                body = KEY_RESPONSE_MARKER + f"({encrypted_des_key})"

                # Send the key back to the requestor so that they can say what they want
                MAIL.send(e["sender"]['email'], e["subject"], body)
        elif e["body"].startswith(KEY_RESPONSE_MARKER):
            _key = keys.get_3des_key(e["sender"]["email"])
            if _key is None or not all(_key):
                # Use my private RSA key to decrypt the DES key
                ckeys = e["body"].strip(KEY_RESPONSE_MARKER).strip()[1:-1].split()

                p, q, d = keys.get_private_rsa_key(MAIL.account.Name)
                rsa = RSA(int(p), int(q))
                rsa.d = int(d)
                print("decrypting")
                pkeys = [
                    bin(rsa.decrypt(int(ck)))[2:] for ck in ckeys
                ]
                pkeys = ['0'*(64-len(k)) + k for k in pkeys]
                # Save it
                keys.save_3des_key(e["sender"]['email'], *pkeys)

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
    pub = " ".join(keys.get_public_rsa_key(MAIL.account.Name))
    body = f"{KEY_REQUEST_MARKER}({pub})"
    MAIL.send(
        user,
        "DAS Request",
        body,
    )
    return "300"


if __name__ == "__main__":
    app.run()
