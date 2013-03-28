Battleship_Game
===============

This game is an implementation of the popular board game, battleship, using 
python. Battleship includes two players, either human vs. human, human vs. 
computer, or computer vs. computer.  The game starts off with 2 players 
placing ships onto their respective ship boards.  After the ship placement 
phase, the firing phase commences.  Each player takes turns firing onto their 
opponents ship board, using their own shots board to mark either a hit or a 
miss.  If the chosen firing location contains an enemy ship, the location is 
marked as a red pegs on the player's shot board as well as the opponent's ship 
board.  If the chosen firing location does not contain an enemy ship, the 
location is marked as a white pegs on the player's shot board as well as the 
opponent's ship board.  Once all the spots on a ship have been hit, a print 
statement will appear in the terminal, indicating who's ship has been sunk and 
which ship has been sunk.  Once a player loses all of his/her ships, the game 
ends, displaying the winner of the game.  

********How To Play********

Begin by selecting the players, they can be either human vs. human, human vs. 
computer, or computer vs. computer.  Four canvases will then appear on the 
screen. For Player vs. Player, the idea is that you will move the respective 
ships board and shots board to either side of the screen.  Screen looking is 
frowned upon. The correct setting is for the lighter blue canvas to be on the 
bottom and the darker blue screen to be on the time but any orientation works. 
To place ships, the human player chooses a point by clicking on a square. 
The next step is to choose an orientation; this is done by choosing another 
square in the direction you want the ship to point. After all ships have been 
placed, the firing phase starts.  To fire, choose a position on your shots 
board, white pegs indicate misses while red pegs indicate hits. After all 
points on a ship have been hit, a statement appears on the terminal indicating 
the ship.  Once a player loses all of his/her ships, the game ends, displaying
the winner of the game.  The game closes with a click on the canvas of the 
winner's shot board. The game closes with a click on the canvas of the 
winner's shot board.

********How To Run********

Type into terminal:

python Battleship.py

Then follow the on screen instructions. 
*IMPORTANT: You must have all of the required files in order to run the game.

********Required Files********

Battleship.py
cs1graphics.py
Board.py
Player.py
GraphicsManager.py
SelectionList.py