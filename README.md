# OOAnalysis-Design

### Installation

Run `git clone https://github.com/theycallmemac/OOAnalysis-Design` in your terminal to clone the project. Once this is done, change directory into the project using `cd OOAnalysis-Design/src`.

To install dependencies, run `pip3 install -r requirements.txt`. If you don't have pip3, install pip3 using `sudo apt-get install python3-pip` on your machine.

After all this, you should be able to run the project.


### Running the Project

#### Using Flask Server
To run the project:
- Ensure your path is as follows: ../OOAnalysis-Design/src
- Run the following command to start up the server: `FLASK_APP=server.py flask run`

Once the server has been started, go to localhost:5000/game in your browser.

#### Using Docker
This project now supports Docker, but can only be used once you have switched over to the `docker` branch.

To run the project using Docker:
- Ensure you are on the correct branch by using `git checkout docker`
- Ensure your path is as follows: ../OOAnalysis-Design/src
- Run the following command to build the container: `docker build -t username/scrabble .`
- Run the following command to run your container: `docker run -d --name scrabble -p 5000:5000 username/scrabble`
- Once the server has been started, go to localhost:5000/game in your browser.

### Usage

Scrabble is to be played between two players, meaning no more than two players may connect to `/game` at any given time. The server tracks which players turn it is. During a turn, players can make a word, swap the letters from their rack, or pass their turn to their opponent.

If you want to place letters on the board to make a word, the format is `("Letter", [ROW, COLUMN])`. For example: `("A", [6, 3])`, or `("A", [3, 3]), ("N", [4, 3])`. 


### Dependencies:

- flask
- flask-cors
- flask-socketio
- eventlet
- gevent
- gevent-websocket
- autopep8
