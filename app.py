import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)
app.static_folder = 'static'

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///beasts.db")

@app.route("/")
def index():
    beasts = db.execute("SELECT * FROM beasts GROUP BY name")
    return render_template("/index.html", beasts=beasts)

@app.route("/index.html")
def indexx():
    beasts = db.execute("SELECT * FROM beasts GROUP BY name")
    return render_template("/index.html", beasts=beasts)

@app.route("/cr.125.html")
def cr125():
    beasts = db.execute("SELECT * FROM beasts WHERE cr = ?", "1/8")
    return render_template("/cr.125.html", beasts=beasts)

@app.route("/cr.25.html")
def cr25():
    beasts = db.execute("SELECT * FROM beasts WHERE cr = ?", "1/4")
    return render_template("/cr.25.html", beasts=beasts)

@app.route("/cr.5.html")
def cr5():
    beasts = db.execute("SELECT * FROM beasts WHERE cr = ?", "1/2")
    return render_template("/cr.5.html", beasts=beasts)

@app.route("/cr1.html")
def cr1():
    beasts = db.execute("SELECT * FROM beasts WHERE cr = ?", "1")
    return render_template("/cr1.html", beasts=beasts)

@app.route("/cr2.html")
def cr2():
    beasts = db.execute("SELECT * FROM beasts WHERE cr = ?", "2")
    return render_template("/cr2.html", beasts=beasts)

@app.route("/cr3.html")
def cr3():
    beasts = db.execute("SELECT * FROM beasts WHERE cr = ?", "3")
    return render_template("/cr3.html", beasts=beasts)

@app.route("/add_beast.html", methods=["GET", "POST"])
def add_beast():
    if request.method == "POST":

        name = request.form.get("name")
        cr = request.form.get("CR")
        hp = int(request.form.get("HP"))
        ac = int(request.form.get("AC"))
        speed = int(request.form.get("speed"))
        str = int(request.form.get("str"))
        dex = int(request.form.get("dex"))
        con = int(request.form.get("con"))
        inte = int(request.form.get("inte"))
        wis = int(request.form.get("wis"))
        cha = int(request.form.get("cha"))
        actions = request.form.get("actions")
        languages = request.form.get("languages")

        # make sure the beast doesnt already exist
        beast_name = db.execute("SELECT * FROM beasts WHERE name = ?", name)
        if beast_name == name:
            return render_template("/add_beast.html")
        else:
        # update beasts.db
            db.execute("INSERT INTO beasts (name, cr, hp, ac, speed, str, dex, con, inte, wis, cha, actions, languages) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", name, cr, hp, ac, speed, str, dex, con, inte, wis, cha, actions, languages)
            return redirect("/")

    else:
        return render_template("/add_beast.html")

@app.route("/beast.html" , methods=["GET", "POST"])
def beast():
    if request.method == "POST":
        name = request.form.get("name")
        beasts = db.execute("SELECT * FROM beasts WHERE name = ?", name)
        return render_template("/beast.html", beasts=beasts)
    else:
        return render_template("/beast.html")