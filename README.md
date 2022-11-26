# das (Deem, Aryee, Stansbury)
_das ist gut_

Desktop application for decentralized secure email communication
## Requirements
- Windows 10
- Microsoft Outlook
  - Utilizing Outlook to handle email sending/recieving means that the users do not need to enter their email account passwords into our application.
  - We believe that the best form of data stewardship is not requesting the data in the first place. While we could eliminate the dependence on 3rd party email clients by sacrificing this principle, we understand that this code does not have the same level of trust as MS Outlook and do not wish to compel users to relinquish that trust to us (or to dig through the code in order to verify our proper handling). This may change in the future once that trust has been established.
  - We do however require the ability to read emails. The code currently reads the past 2 days worth of emails [outlook.py#L42](https://github.com/JoelStansbury/das/blob/main/das/outlook/outlook.py#L42). This is unavoidable
  - Similarly we require the ability to send emails on behalf of the user (using MS Outlook as a proxy) [outlook.py#L81](https://github.com/JoelStansbury/das/blob/main/das/outlook/outlook.py#L81). This is also an unavoidable requirement.
  - We do not, however store any email data to any local files. The unencrypted text exists in memory for the duration of the session untill the application is stopped.
  - There is no external communication except what is required between MS Outlook and the javascript application


> __DISCLAIMER 1:__ Keys shared between users are stored in an unencrypted file `das/key_manager/keys.csv`. If an encrypted conversation is to be rendered _practically_ un-decryptable, it is required that both users deleted the line corresponding to the other user in their `keys.csv`. It is also not read-write protected, so this is something that must be fixed before the tool is to be used in a critical setting.
> __DISCLAIMER 2:__ This is still vulnerable to Man-in-the middle attacks carried out by either MS Outlook or the email service providers. Mitigating or eliminating this threat is a topic for future work.


- [flask](https://pypi.org/project/Flask/) _application host_
- [flask-cors](https://pypi.org/project/Flask-Cors/)
- [sympy](https://pypi.org/project/sympy/) _large prime number generation_

These can be obtained via pypi or conda
#### Pip
```bash
pip install flask flask-cors sympy
pip install -e .
python -m das.app
```
#### Conda
```bash
conda env create -f environment.yml -p ./.venv
conda activate ./.venv
pip install .
python -m das.app
```

## Setup
- Clone the repo
- `cd` into the folder
- `pip install -e .`

## Running the App
`python -m das.app`

OR

`flask --app das/app.py --debug run`

> on unix this is you'll need `python3 -m das.app`

and navigate to http://localhost:5000 to see the website
