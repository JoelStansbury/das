import code
from typing import Union, List
from pathlib import Path
import json
from datetime import datetime, timedelta

import win32com.client as win32
import pythoncom

# 'Tuesday Sep/13 23:22'
# DATETIME_FORMAT = "%A %b/%d %H:%M"
DATETIME_FORMAT = "%y-%m-%d %H:%M"
HERE = Path(__file__).parent
MSG_CACHE = HERE / "msg_cache.json"

if not MSG_CACHE.exists():
    print(f"First time setup, creating cache at {MSG_CACHE}")
    MSG_CACHE.touch()
    with MSG_CACHE.open("w") as f:
        json.dump({}, f)

with MSG_CACHE.open("r") as f:
    CACHE = json.load(f)


def save_cache():
    with MSG_CACHE.open("w") as f:
        json.dump(CACHE, f)


def email_hash(email: win32.CDispatch):
    return email.Subject + str(email.ReceivedTime) + email.Sender.Address


def email_to_dict(email):
    return {
        "id": email_hash(email),
        "sender": {
            "name": email.Sender.Name,
            "email": email.SenderEmailAddress,
        },
        "recipients": [
            {"name": r.Name, "email": r.Address} for r in email.Recipients
        ],
        "cc": email.CC,
        "subject": email.Subject,
        "body": email.Body,
        "recieved": email.ReceivedTime.Format(DATETIME_FORMAT),
    }


class Outlook:
    def __init__(self):
        self.app = win32.Dispatch("Outlook.Application", pythoncom.CoInitialize())
        self.select_account(0)

    def get_emails(self, folder_name):
        min_dt = datetime.now() - timedelta(days=2)
        min_dt_str = min_dt.strftime(DATETIME_FORMAT)
        email_objs = self.folders[folder_name].Items
        N = len(email_objs)
        if N==0: return []
        i=1
        last = email_to_dict(email_objs[N-i])
        while last["recieved"] > min_dt_str:
            yield last
            i += 1
            last = email_to_dict(email_objs[N-i]) 
        
        i = 0
        last = email_to_dict(email_objs[i])
        while last["recieved"] > min_dt_str:
            yield last
            i += 1
            last = email_to_dict(email_objs[i])

    @property
    def accounts(self):
        result = []
        for i, account in enumerate(self.app.Session.Folders):
            if not account.Name.startswith("Public Folders - "):
                result.append((account.Name, i))
        return result

    def select_account(self, i):
        self.account_idx = i
        self.account = self.app.Session.Folders[i]
        self.account_name = self.account.Name
        if self.account_name not in CACHE:
            CACHE[self.account_name] = {}
        self.folders = {}
        for f in self.account.Folders:
            self.folders[f.Name] = f
            if f.Name not in CACHE[self.account_name]:
                CACHE[self.account_name][f.Name] = {}

    def send(self, to: Union[List[str], str], subject, body):
        if isinstance(to, str):
            to = [to]
        print(f"Sending message from ({self.account.Name}) to ({to})")
        msg = self.app.CreateItem(0)
        msg.To = "; ".join(to)
        msg.Subject = subject
        msg.Body = body
        # Set sender to currently active account (as opposed to the default for Outlook)
        msg._oleobj_.Invoke(
            64209,
            0,
            8,
            0,
            self.app.Session.Accounts[self.account.Name]
        )
        msg.Send()

    def delete(self, id, folder_name):
        min_dt = datetime.now() - timedelta(days=3)
        min_dt_str = min_dt.strftime(DATETIME_FORMAT)
        email_objs = self.folders[folder_name].Items
        N = len(email_objs)
        if N==0: return []
        i=1
        last = email_to_dict(email_objs[N-i])
        while last["recieved"] > min_dt_str:
            if last["id"] == id:
                email_objs[N-i].delete()
                return
            i += 1
            last = email_to_dict(email_objs[N-i]) 
        
        i = 0
        last = email_to_dict(email_objs[i])
        while last["recieved"] > min_dt_str:
            if last["id"] == id:
                email_objs[N-i].delete()
                return
            i += 1
            last = email_to_dict(email_objs[i])

if __name__ == "__main__":
    ol = Outlook()
    ol.select_account(0)
    print(len(list(ol.get_emails("Inbox"))))
    ol.send("stansbury.joel@gmail.com", "2", "3")
    # code.interact(local=locals())
