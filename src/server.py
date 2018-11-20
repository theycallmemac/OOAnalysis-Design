# Import flask and socket libraries
from flask import Flask, render_template
from flask_socketio import SocketIO

# Import Game Classes
from classes.board import Board
from classes.letter import Letter
from classes.square import Square
from classes.rack import Rack 
from classes.player import Player 
from classes.word import Word 
from classes.bag import Bag

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@socketio.on('my event')
def handle_message(message):
    print(message)

@app.route('/')
def start():
    return "start"

@app.route('/move')
def move():
    return "move" 

@app.route('/swap')
def swap():
    return "swap" 

@app.route('/skip')
def skip():
    return "skip"

if __name__ == '__main__':
    # Encapsulates the start up of the web server
    socketio.run(app, port="5000", host="0.0.0.0")
