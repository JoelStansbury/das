# das (Deem, Aryee, Stansbury)
_das ist gut_

Cross platform desktop application for encrypting and digitally signing files
## Requirements
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
