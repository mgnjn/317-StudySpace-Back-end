# 317-StudySpace-Back-end

CP317 Team 2 StudySpace repo for the back-end

Admin Entry:
http://localhost:8000/admin

User:host
Password:password

Health Check Page:
http://127.0.0.1:8000/ht

## Installation:

Make sure you have Python 3 installed.

Then, in Terminal / Command Prompt do the following:

### Step 1: Set up a virtual environment

Set up a python virtual environment:

**For Mac/Linux:**
`python3 -m venv ~/.virtualenvs/djangodev`

**For Windows**
`py -m venv %HOMEPATH%\.virtualenvs\djangodev`

"djangodev" is just an arbitrary name, you could name it anything.

and then activate it:

**For Mac/Linux:**
`source ~/.virtualenvs/djangodev/bin/activate`

if the source command is not available, you can try using a dot instead:
`. ~/.virtualenvs/djangodev/bin/activate`

**For Windows:**
`%HOMEPATH%\.virtualenvs\djangodev\Scripts\activate.bat`

### Step 2: Install dependencies

Clone this repo and cd into "317-StudySpace-Back-End/StudySpace"

Install the dependencies using pip3 (for python3) in the terminal:
`pip3 install -r requirements.txt`

### Step 3: Run the server

Make sure you are in this directory "317-StudySpace-Back-End/StudySpace" in the terminal and type:
`python3 manage.py runserver`

Server will run on 127.0.0.1:8000

## Other Notes:

Any time new dependencies are added, the requirements.txt file must be modified. Here's how to do it:

- In the terminal type `pip3 freeze > requirements.txt`
- This will rewrite the file with the new dependencies.

See [this](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1) for more details.

Also, the virtual environment must be activated everytime a new terminal window opens.