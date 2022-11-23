
import csv
import os
from pathlib import Path
from random import random
from das.algorithms import RSA

field_names = [
        "User",
        "RSA Public Key",
        "RSA Private Key",
        "DES Key 1",
        "DES Key 2",
        "DES Key 3"
    ]


def get_private_rsa_key(my_email_address):
    with open("keys.csv", newline='') as csvfile:
        current_keys = csv.DictReader(csvfile, fieldnames=field_names)
        for rows in current_keys:
            if rows['User'] == my_email_address:
                return rows['RSA Private Key']


def get_public_rsa_key(my_email_address):
    with open("keys.csv", newline='') as csvfile:
        current_keys = csv.DictReader(csvfile, fieldnames=field_names)
        for rows in current_keys:
            if rows['User'] == my_email_address:
                return rows['RSA Public Key']


def get_3des_key(other_user):
    # return key1, key2, key3
    with open("keys.csv", newline='') as csvfile:
        current_keys = csv.DictReader(csvfile, fieldnames=field_names)
        for rows in current_keys:
            if rows['User'] == other_user:
                return rows['DES Key 1'], rows['DES Key 2'], rows['DES Key 3']


def save_3des_key(other_user, key1, key2, key3):
    save_keys("", "", key1, key2, key3, other_user)


def generate_rsa_key(my_email_address):
    generator = RSA()

    pub_key = "(" + str(generator.n) + " " + str(generator.k) + ")"
    priv_key = "(" + str(generator.p) + " " + str(generator.q) + " " + str(generator.d) + ")"

    save_keys(pub_key, priv_key, "", "", "", my_email_address)


def generate_des_key(other_user):
    s = []
    for i in range(3):
        s.append("")
        for j in range(64):
            if random() > .5:
                s[i] += "1"
            else:
                s[i] += "0"
    save_3des_key(other_user, s[0], s[1], s[2])


def save_keys(rsa_pubkey, rsa_prikey, des_key_1, des_key_2, des_key_3, sender_name):
    keys = []
    skip = True
    with open("keys.csv", newline='') as csvfile:
        current_keys = csv.DictReader(csvfile, fieldnames=field_names)
        for rows in current_keys:
            if not skip:
                keys.append(rows)
            else:
                skip = False

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


def main():
    generate_rsa_key("rtdeem@gmail.com")
    generate_des_key("rdeem@students.kennesaw.edu")
    print(get_public_rsa_key("rtdeem@gmail.com"))
    print(get_private_rsa_key("rtdeem@gmail.com"))

    print(get_3des_key("rdeem@students.kennesaw.edu"))


if __name__ == '__main__':
    main()
