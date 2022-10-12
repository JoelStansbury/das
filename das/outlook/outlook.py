import code
from typing import Union, List
from pathlib import Path
import json

import win32com.client as win32

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


class Outlook:
    def __init__(self):
        self.app = win32.Dispatch("Outlook.Application")
        self.select_account(0)

    def load(self, folder_name):
        email_objs = self.folders[folder_name].Items
        print(f"# EMAILS: {len(email_objs)}")

        # Outlook seems to use a bespoke dynamic array datastructure.
        # New items are added to the end of the list, but otherwise is
        # sorted by date recieved.
        N = len(email_objs)
        i = N - 1
        while i >= 0:
            try:
                email = email_objs[i]
                _id = email_hash(email)
                break
            except:  # get error
                i -= 1
        while (
            email is not None
            and _id not in CACHE[self.account_name][folder_name]
            and i >= 0
        ):
            try:
                CACHE[self.account_name][folder_name][_id] = {
                    "id": _id,
                    "sender": {"name": email.Sender.Name, "email": email.SenderEmailAddress},
                    "recipients": [{"name": r.Name, "email":r.Address} for r in email.Recipients],
                    "cc": email.CC,
                    "subject": email.Subject,
                    "body": email.Body,
                    "recieved": email.ReceivedTime.Format(DATETIME_FORMAT)
                }
            except:  # read error (could not read email)
                pass
            while i >= 0:  # scan for next processable email
                i -= 1
                try:
                    email = email_objs[i]
                    _id = email_hash(email)
                    break  # add email to cache
                except:  # get error (could not get info about email)
                    pass

        # Now, start from the end of the list and work backwards until
        # hitting a previously cached message
        i = 0
        while i <= N:
            try:
                email = email_objs[i]
                _id = email_hash(email)
                break
            except:  # get error (could not get info about email)
                i += 1
        while _id not in CACHE[self.account_name][folder_name]:
            try:
                CACHE[self.account_name][folder_name][_id] = {
                    "id": _id,
                    "sender": {"name": email.Sender.Name, "email": email.SenderEmailAddress},
                    "recipients": [{"name": r.Name, "email":r.Address} for r in email.Recipients],
                    "cc": email.CC,
                    "subject": email.Subject,
                    "body": email.Body,
                    "recieved": email.ReceivedTime.Format(DATETIME_FORMAT)
                }
            except:  # read error
                pass
            while i <= N:
                i += 1
                try:
                    email = email_objs[i]
                    _id = email_hash(email)
                    break
                except:  # get error
                    pass
        save_cache()

    def get_emails(self, folder_name):
        self.load(folder_name)
        emails = sorted(
            CACHE[self.account_name][folder_name].values(),
            key=lambda x: x["recieved"],
            reverse=True
        )
        return emails

    @property
    def accounts(self):
        result = []
        for i, account in enumerate(self.app.Session.Folders):
            result.append((account.Name, i))
        return result

    def select_account(self, i):
        self.account_idx = i
        self.account = self.app.Session.Folders[self.account_idx]
        self.account_name = self.account.Name
        if self.account_name not in CACHE:
            CACHE[self.account_name] = {}
        self.folders = {}
        for f in self.account.Folders:
            self.folders[f.Name] = f
            if f.Name not in CACHE[self.account_name]:
                CACHE[self.account_name][f.Name] = {}

    # @property
    # def rules(self):
    #     return self.account.Store.GetRules()

    # @property
    # def rule_names(self):
    #     rules = self.rules
    #     return [rules.Item(i).Name for i in range(1, rules.Count+1)]

    # def setup_rule(self):
    #     rules = self.account.Store.GetRules()
    #     r = rules.Create("DAS")
    #     body_condition = r.Conditions.Body
    #     body_condition.Enabled = True
    #     TODO: create text condition, create folder, move to folder
    #     rules.Save()

    def send(self, to: Union[List[str], str], subject, body):
        if isinstance(to, str):
            to = [to]
        msg = self.app.CreateItem(0)
        msg.To = "; ".join(to)
        msg.Subject = subject
        msg.Body = body
        msg.Send()

    def reply(self, email, subject, body):
        self.send(
            to=email["sender"],
            subject=subject,
            body=body,
        )

    def reply_all(self, email, subject, body):
        self.send(
            to= [email["sender"], email["cc"]],
            subject=subject,
            body=body,
        )


if __name__ == "__main__":
    ol = Outlook()
    ol.select_account(0)
    code.interact(local=locals())
