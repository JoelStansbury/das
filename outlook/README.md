## Outlook
Python package for reading and sending emails through MS Outlook.

## Usage
```python
from outlook import Outlook
mail = Outlook()
```
> This will prompt you to initialize outlook if you have not done so already
* Display available accounts with `mail.accounts`
* Select an account to load with `mail.select_account(i)` where `i` is the index of the account you wish to use
* Display available folders with `mail.folders`
* Use `mail.load("Inbox")`
