from flask import request, Flask
import json


import os


app = Flask(__name__)


def addUsertoFile(name_pass):
    if os.path.exists("./newuserlog/users.txt") == False:
        f = open("./newuserlog/users.txt", "w")
        f.write(name_pass+"\n")
    else:
        with open("./newuserlog/users.txt", "a") as f:
            f.write(name_pass+"\n")


def retrieveFromFile():
    users = dict()
    if os.path.exists("./newuserlog/users.txt") != False:
        f = open("./newuserlog/users.txt", "r")
        for line in f:
            details = line.split("-")
            name = details[0]
            password = details[1]
            users[name] = password
    return users


@app.route("/")
def hello():
    return f"Welcome to the index page"


@app.route("/newuser/<userdetails>")
def newUser(userdetails):
    usersDict = retrieveFromFile()
    details = userdetails.split("-")
    uname = details[0]
    password = details[1]

    if uname not in usersDict.keys():
        addUsertoFile(userdetails)
        usersDict[uname] = password
        return f"Added new user"

    return f"User already exists.."


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=9000)
