# Requirements
- We have been asked to implement a word game which is very similar to Scrabble. 

- The game shall be an online game, that is to say that players will be able to play with each other from remote sites on the Internet.

- This game will therefore, take the client/server structure where the client shows one player's view of the game while the server allows communication between the players and manages the game itself.

- The server will match two players and begin a game once two players have joined. This will create a traditional 15x15 Scrabble board, two 1x7 tile racks (one for each user), and a bag, which will contain all the playable letter tiles.

- The board will consist of regular values tiles, and special coloured multiplier tiles. Depending on where a word is placed a multiplier may be applicable. These special tiles consist of:
    - Light Blue: Doubled Letter Value
    - Dark Blue: Tripled Letter Value
    - Light Red: Doubled Word Value
    - Dark Red: Tripled Word Value
 
- Along with this, there is a star tile in teh center of the board, through which the first word place on the board must pass. The first player is chosen at random by the server. Player one attempts to make a word that goes through the star and earnS max points on the board. If the player is unable or not willing to place a word, a player can either:
    - 1. Pass their turn to the other player.
    - 2. Swap N tiles from their rack for N tiles from the bag.

- When Player 1 ceases their move, Player 2 then follows the process prior with the key difference of having to try append/integrate with a word on the board since the star is no longer available. 

- There are three valid end conditions to a given game. The proccess of making moves continues until either:
    - 1. No possible words can be played.
    - 2. Board is already full of letter tiles.
    - 3. No tiles remain in the bag and the rack.

- A Score is calculated by the server based on the tiles and multipliers on which they may or may not sit. A winner declared by the server as the player with the highest score. The game is closed by the server after this.

