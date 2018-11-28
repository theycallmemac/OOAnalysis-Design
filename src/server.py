#Import flask and socket libraries
from flask import Flask, render_template
from flask_socketio import SocketIO
import json

# Import Game Classes
from src.classes.board import Board
from src.classes.letter import Letter
from src.classes.rack import Rack 
from src.classes.player import Player 
from src.classes.word import Word 
from src.classes.bag import Bag


board = Board()
word = Word("2342")
testw = Word("BOATED")
connection_count = 0

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@socketio.on('onconnect')
def handle_onconnect(message):
	global connection_count
	connection_count += 1
	print(message)

@socketio.on('skip')
def handle_skip(code):
	code = json.dumps(code)
	code = json.loads(code)
	print(board.board)

@socketio.on('move')
def handle_move(move):
	move = json.dumps(move)
	move = json.loads(move)
	move_list = eval(move["val"])
	print(type(move_list[0][1]))
	board.placeLetters(move_list)
	print(board.board)
	socketio.emit('response', board.board)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
	if connection_count >= 2:
		print("REFUSED")
		return "error.html"
	return render_template("game.html")


if __name__ == '__main__':
    # Encapsulates the start up of the web server
    socketio.run(app, port="5000", host="0.0.0.0")
