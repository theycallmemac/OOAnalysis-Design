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
players = []

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@socketio.on('onconnect')
def handle_onconnect(message):
	global connection_count
	if len(players) == 2:
		return render_template("error.html")
	print("COUNT", connection_count)
	new_player = Player(connection_count, getTurn())
	players.append(new_player)
	socketio.emit('idset', [new_player.id, new_player.isTurn])
	connection_count += 1
	print(message)

def swapTurn():
	global players
	for player in players:
		print("ATTEMPT", player.isTurn, player.id)
		if player.isTurn == False:
			player.isTurn = True
			print(player.isTurn, player.id)
		else:
			player.isTurn = False
			print(player.isTurn, player.id)


def getTurn():
	global players
	print("LEN", len(players))
	if len(players) == 0:
		return True
	return False

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
	swapTurn()
	#print(players[0].id, )
	socketio.emit('moveresponse', [board.board, players[0].isTurn, players[1].isTurn])

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
