
import csv
import os
from pathlib import Path

def get_private_aes_key(my_email_address):
    pass

def get_public_aes_key(my_email_address):
    pass

def get_3des_key(other_user):
    # return key1, key2, key3
    pass

def save_3des_key(other_user, key1, key2, key3):
    pass

def generate_aes_key(my_email_address):
    pass

def generate_des_key(my_email_address):
    pass

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
