# das (Deem, Aryee, Stansbury)
Cross platform desktop application for encrypting and digitally signing files

## Setup
We're using conda to manage all our development enviroment.

1. Install Anaconda or Miniconda
2. Clone the repo
3. Open a conda terminal
4. `cd PATH/TO/REPO`
5. `conda env update -f environment.yml -p ./.venv`
6. `conda activate ./.venv` You'll need to run this every time
   1. (optional) make a shortcut to aleviate the hassle of running `conda activate ./.venv`
      1. In your start menu, search for `Anaconda Prompt (Miniconda or Anaconda)`
      2. Right click -> open file location
      3. Find the file, and `ctrl` + `c` to copy it
      4. paste a copy wherever you find convinient
      5. right click the new shortcut -> Properties
      6. append `&& cd PATH/TO/REPO && conda activate ./.venv` to the target field
         1. It helps to do this in a text editor
7. Once we make the package you will finalize the setup with `pip install -e .` (but not yet)

