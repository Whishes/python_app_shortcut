# get venv installed
import os

print("--> Installing venv")
install_venv = "python3 -m venv venv"
os.system(install_venv)

# check to see if in venv/is installed
def venv_installed_correctly():
    return os.path.isfile("venv/bin/activate")


if venv_installed_correctly():
    print("--> You have successfully installed venv")

    # check if install.txt exists, if not default to normal Flask install
    if os.path.isfile("install.txt"):
        # loop over txt file and install each line item
        installTxt = open("install.txt", "r")
        installItems = installTxt.readlines()

        for line in installItems:
            print(f"--> Installing {line}")
            install_Line = f"venv/bin/python -m pip install {line}"
            os.system(install_Line)
            print(f"--> You have successfully installed {line}")
    else:
        # default to flask install
        # pip install Flask
        print("--> Could not find install.txt so defaulting to default install")
        print("--> Installing Flask")
        install_Flask = "venv/bin/python -m pip install Flask"
        os.system(install_Flask)
        print("--> You have successfully installed Flask")

    # create app.py file
    print("--> Creating files/folders")
    create_app = open("app.py", "w")

    # fill out basic app.py template
    create_app.write('''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    ''')
    create_app.close()

    # create templates folder
    try:
        os.mkdir("templates")
    except OSError as error:
        print(error)

    # create static folder, create images + css folder
    try:
        os.mkdir("static")
        os.mkdir("static/images")
        os.mkdir("static/css")
    except OSError as error:
        print(error)

    # create styles.css file in the css folder
    create_css = open("static/css/styles.css", "w")
    create_css.write('''
* {
    margin: 0;
    padding: 0;
}

h1 {
    color: green;
}
    ''')
    create_css.close()
    # create index.html file
    create_html = open("templates/index.html", "w")
    
    # fill out index.html file w/ basic structure w/ link to styles.css
    create_html.write('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Template Web App</title>
    <link rel="stylesheet" href="./static/css/styles.css">
</head>

<body>
    <h1>Template Web App</h1>
    <p>the heading will be green if css is linked correctly</p>
</body>
    ''')
    create_html.close()
    print("--> Files/Folders have been created")

    #Alert user that everything is finished
    print("--> Everything has finished installing and all files/folders have been created")
    #print("--> NOTE: For now you will need to re-activate venv if you wish to install more packages in venv")

    # activate venv
    os.system("/bin/bash --rcfile venv/bin/activate")
else:
    print("--> Error: Venv has not installed correctly")
    print("--> NOTE: Check the command on line 5 of shortcut.py to make sure the command is correct")
    print("--> NOTE: If the command is correct, please check your installation of python and the like")
    #print("check if the filepath to activate venv is correct in line 9")