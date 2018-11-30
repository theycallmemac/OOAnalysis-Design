# OOAnalysis-Design

### Installation

Run `git clone https://github.com/theycallmemac/OOAnalysis-Design` in your terminal to clone the project. Once this is done, change directory into the project using `cd OOAnalysis-Design/src`.

To install dependencies, run `pip3 install -r requirements.txt`. If you don't have pip3, install pip3 using `sudo apt-get install python3-pip` on your machine.

After all this, you should be able to run the project.


### Running the Project

#### Using Flask Server
To run the project:
- Set the environable variable FLASK_APP using `FLASK_APP=server.py`
- Run `flask run` to start up the server

#### Using Docker
Docker is not yet supported for this project.


Once the server has been started, go to localhost:5000/game in your browser.

### Usage

Scrabble is to be played between two players, meaning no more than two players may connect to `/game` at any given time. The server tracks which players turn it is. During a turn, players can make a word, swap the letters from their rack, or pass their turn to their opponent.

If you want to place letters on the board to make a word, the format is `("Letter", [ROW, COLUMN])`. For example: `("A", [6, 3])`, or `("A", [3, 3]), ("N", [4, 3])`. 


### Dependencies:

- flask
- flask-socketio
- eventlet
- gevent
- gevent-websocket
