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


def get(obj, attr):
    return getattr(obj, attr, )

def email_to_dict(email):
    sender = getattr(email, "Sender", "")
    return {
        "sender": {
            "name": getattr(sender, "Name", "") ,
            "email": getattr(sender, "Address", "")
        },
        "recipients": [
            {"name": r.Name, "email": r.Address} for r in email.Recipients
        ],
        "cc": getattr(email, "CC", ""),
        "subject": email.Subject,
        "body": email.Body,
        "recieved": email.ReceivedTime.Format(DATETIME_FORMAT),
    }


class Outlook:
    def __init__(self):
        self.app = win32.Dispatch("Outlook.Application", pythoncom.CoInitialize())
        self.select_account(self.accounts[0])

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
        for account in self.app.Session.Folders:
            if not account.Name.startswith("Public Folders - "):
                result.append(account.Name)
        return result

    def select_account(self, account_name):
        for f in self.app.Session.Folders:
            if f.name == account_name: 
                self.account = f
                self.account_name = account_name
                break

        self.folders = {}
        for f in self.account.Folders:
            self.folders[f.Name] = f

    def send(self, to: Union[List[str], str], subject, body):
        if isinstance(to, str):
            to = [to]
        print(f"Sending message from ({self.account.Name}) to ({to}): {body}")
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
    ol.select_account("stansbury.joel@gmail.com")
    e = list(ol.get_emails("Inbox"))[0]
    print(e["sender"])
    # ol.send("stansbury.joel@gmail.com", "2", "3")
    # code.interact(local=locals())
