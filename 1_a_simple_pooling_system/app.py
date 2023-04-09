""" 
A simple web app which gives random name from the here list after clicking on the pick button 
"""


from flask import Flask, render_template
from random import randint


app = Flask(__name__)

hero = ["Lion",
        "Cat",
        "Dog",
        "Panda",
        "Horse",
        "Blank"]


@app.route('/index')
def index():
    return render_template("index.html", hero=hero)


@app.route('/pick')
def pick():
    num = randint(0, len(hero)) - 1
    return render_template("index.html", hero=hero, h=hero[num])

app.run()