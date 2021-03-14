from flask import render_template, request, redirect
from app import app 
from app.models.game import *
from app.models.player import *

@app.route('/players')
def index():
    return render_template('index.html', title="PRS", players=players)

@app.route('/players', methods=['POST'])
def add_player():
    name = request.form['name']
    choice = request.form['choice']
    newplayer = Player(name=name, choice=choice)
    add_new_player(newplayer)
    return redirect('/players')