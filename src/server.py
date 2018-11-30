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
from copy import deepcopy


# Initialize racks
def init_racks():
	global racks
	global bag
	for x in range(2):
		letters = []
		for i in range(7):
			letters.append(bag._remove())
		new_rack = Rack(letters)
		racks.append(new_rack)

#Initialize Everything
board = Board()
bag = Bag()
racks = []
init_racks()
word = Word("INITIALIZECLASSVARIABLES")
connection_count = 0
players = []


# Initialize Flask App
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


# Player connection handler
@socketio.on('onconnect')
def handle_onconnect(message):
	global connection_count
	global racks
	if len(players) == 2:
		return render_template("error.html")
	new_player = Player(connection_count, getTurn(), racks[connection_count])
	players.append(new_player)
	socketio.emit('idset', [new_player.id, new_player.isTurn, new_player.rack.toArray(), board.board])
	connection_count += 1
	print(message)

# Swapping handler
def swapTurn():
	global players
	for player in players:
		if player.isTurn == False:
			player.isTurn = True
		else:
			player.isTurn = False


#Pass Handler
@socketio.on('pass')
def handle_pass(req):
	socketio.emit('passresponse')

# Turn Handler
def getTurn():
	global players
	if len(players) == 0:
		return True
	return False


#Skip Handler
@socketio.on('skip')
def handle_skip(code):
	code = json.dumps(code)
	code = json.loads(code)


#Top score handler
def get_top_score():
	score = 0
	winner = -1
	for player in players:
		if player.score >= score:
			score = player.score
			winner = player.id
	return winner

#Swap Request Handler
@socketio.on('swap')
def handle_swap(req):
	global bag
	req = json.dumps(req)
	req = json.loads(req)
	p_id = req["id"]
	p_rack = req["rack"]
	players[p_id].rack.swap(p_rack, bag)
	if swap_end_state(p_rack):
		winner = get_top_score()
		socketio.emit("gameover", [winner, players[winner].score])
	swapTurn()
	socketio.emit('swapresponse', [players[p_id].id, players[p_id].rack.toArray(), players[0].isTurn, players[1].isTurn])


# Update Rack Handler
def update_rack(player, movelist):
	global bag
	rack = player.rack
	chars = []
	from_bag = []
	for x in range(len(movelist)):
		if not bag.isEmpty():
			letter = bag._remove()
			if letter != False:
				from_bag.append(letter)
	for move in movelist:
		chars.append(move[0])
	for char in chars:
		if char in rack.toArray():
			rack.removeLetter(char)
	for letter in from_bag:
		rack.add(letter)
	player.rack = rack


# Checks for end state
def move_end_state(player, moves):
	global bag
	return len(moves) > bag.length

# Checks for end state
def swap_end_state(rack):
	global bag
	return len(rack) > bag.length


# Move request handler
@socketio.on('move')
def handle_move(move):
	move = json.dumps(move)
	move = json.loads(move)
	move_list = eval(move["val"])
	if move_end_state(players[move["id"]], move_list):
		return render_template("winner.html")
	before_state = deepcopy(board.board)
	print(type(move_list[0][1]))
	words = board.placeLetters(move_list)
	if board.board != before_state:
		update_rack(players[move["id"]], move_list)
	players[move["id"]].updateScore(words)
	swapTurn()
	socketio.emit('moveresponse', [board.board, players[move["id"]].id, players[move["id"]].rack.toArray(), players[0].isTurn, players[1].isTurn])


# Routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
	if connection_count >= 2:
		return "error.html"
	return render_template("game.html")


if __name__ == '__main__':
    # Encapsulates the start up of the web server
    socketio.run(app, port="5000", host="0.0.0.0")
