# Import flask and socket.io
from flask import Flask, render_template
from flask_socketio import SocketIO

# Import classes
# from classes.square import Square
# from classes.letter import Letter
# from classes.word import Word
# from classes.player import Player
# from classes.board import board
# from classes.rack import Rack 
# from classes.bag import Bag


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello():
    return "Hello"

@socketio.on('my event')
def handle_message(message):
    print(message)

if __name__ == '__main__':
    socketio.run(app)