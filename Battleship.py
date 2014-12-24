#
#Darrel Jiang
#Professor Clair
#CSCI 150 MTWF(9:00-9:50am)
#
#The main Battleship class. Initializes the game.
#
#

from Board import *
from Player import *
from GraphicsManager import *

class Battleship():
    def __init__(self):
	"""Creates a game of Battleship with either a human vs. human, human vs. computer, or computer vs. computer"""
	
	playing = True
	
	#Creates a list of player types, shows up on menu
	playertypenames=['Human','Computer']
	
	#Initializes 2 lists of types of players for the menu selection, one is for the first selection and the other list is for the second selection.
	playertypes = [HumanPlayer(),ComputerPlayer()]
	othertypes = [HumanPlayer(), ComputerPlayer()]
	
	#Initializes the count needed to determine if a ship is sunk (Only for 2 players)
	a1 = 1
	b1 = 1
	s1 = 1
	d1 = 1
	p1 = 1
	a2 = 1
	b2 = 1
	s2 = 1
	d2 = 1
	p2 = 1
	
	#Initializes the value for turns
	turn = 1
	
	#The main loop for the game of battleship.  Initializes the required resources and allows for players to place ships.
	while playing:
	  
		#The main menu that shows up when battleship is initialized. Closes after selections have been made.
		menu = GraphicsManager('skyblue3',1,1)
		p1type = menu.selectFromList('Select Player 1', playertypenames)
		p2type = menu.selectFromList('Select Player 2', playertypenames)
		menu.returnBoard().close()
		
		#Initializes the 2 players.
		player1 = playertypes[p1type]
		player2 = othertypes[p2type]
		
		#Initializes the graphics for the Ships Board and the Shots Board for both players.
		gShips1 = GraphicsManager()
		gShots1 = GraphicsManager('royalblue3')
		gShips2 = GraphicsManager()
		gShots2 = GraphicsManager('royalblue3')
		
		#Allows for both players to place their ships on the appropriate board.
		print 'Player 1, Please place your ships on your Ship Board (Battleship<1>)'
		player1.placeShips(gShips1)
		print 'Player 2, Please place your ships on your Ship Board (Battleship<3>)'
		player2.placeShips(gShips2)
		
		#Initializes the text based Ships Board and Shots Board for both players. It runs in the background of the game and cannot be seen by the players.
		p1ships = player1.getShipBoard()
		p1shots = player1.getShotBoard()
		p2ships = player2.getShipBoard()
		p2shots = player2.getShotBoard()
		
		over = False
		
		#Game loop that allows for players to fire onto boards until a player has no more ships
		while not over:
		  
			#Allows for player 1 to choose a position to fire.
			print "Player 1's turn to fire, turn number: " + str(turn)
			player1.fire(p2ships,p1shots,gShips2,gShots1,gShips2)
			
			#---Checks if the shot sinks any of the opposing player's ships---
			
			  #Checks for the Aircraft Carrier
			if a1 > 0:
				if p2ships.isSunk(0):
					print "Player 2's Aircraft Carrier has been sunk!"
					a1 -= 1
					
			  #Checks for the Battleship
			if b1 > 0:
				if p2ships.isSunk(1):
					print "Player 2's Battleship has been sunk!"
					b1 -= 1
				
			  #Checks for the Submarine
			if s1 > 0:
				if p2ships.isSunk(2):
					print "Player 2's Submarine has been sunk!"
					s1 -= 1
					
			  #Checks for the Destroyer
			if d1 > 0:
				if p2ships.isSunk(3):
					print "Player 2's Destroyer has been sunk!"
					d1 -= 1
					
			  #Checks for the Patrol Boat
			if p1 > 0:
				if p2ships.isSunk(4):
					print "Player 2's Patrol Boat has been sunk!"
					p1 -= 1
			
			#Checks if that shots sinks all of the last ship, if it does, the opposing player loses and the game ends
			if p2ships.lostGame():
				result = 'Player 1 Wins!'
				
				#Displays the graphics that player 1 has won
				gShots1.displayResult(gShips1.returnBoard(),gShots2.returnBoard(),gShips2.returnBoard(),result)
				
				#Ends the game.
				over = True
				playing = False
			
			#Allows for player 2 to choose position to fire.
			print "Player 2's turn to fire, turn number: " + str(turn)
			player2.fire(p1ships,p2shots,gShips1,gShots2,gShips1)
			
			#---Checks if the shot sinks any of the opposing player's ships---
			
			#Checks for the Aircraft Carrier
			if a2 > 0:
				if p1ships.isSunk(0):
					print "Player 1's Aircraft Carrier has been sunk!"
					a2 -= 1
					
			#Checks for the Battleship
			if b2 > 0:
				if p1ships.isSunk(1):
					print "Player 1's Battleship has been sunk!"
					b2 -= 1
					
			#Checks for the Submarine
			if s2 > 0:
				if p1ships.isSunk(2):
					print "Player 1's Submarine has been sunk!"
					s2 -= 1
					
			#Checks for the Destroyer
			if d2 > 0:
				if p1ships.isSunk(3):
					print "Player 1's Destroyer has been sunk!"
					d2 -= 1
					
			#Checks for the Patrol Boat
			if p2 > 0:
				if p1ships.isSunk(4):
					print "Player 1's Patrol Boat has been sunk!"
					p2 -= 1
					
			turn += 1
			#Checks if that shots sinks all of the last ship, if it does, the opposing player loses and the game ends.		
			if p1ships.lostGame():
				result = 'Player 2 Wins!'
				
				#Displays the graphics that player 1 has won
				gShots2.displayResult(gShips1.returnBoard(),gShots1.returnBoard(),gShips2.returnBoard(),result)
				
				#Ends the game.
				over = True
				playing = False
					
		
if __name__ == '__main__':
	Battleship()
	"""def player_select():
	  print 'Select PLayer'
	  print '0) Human'
	  print '1) Computer'
	  player = None
	  while not player:
		instr = raw_input('Please choose type of player: ')
		try:
		  selection = int(instr)
		  possible = [HumanPlayer(),ComputerPlayer()]
		  player = possible[selection]
		except IndexError, ValueError:
		  player = None
	  return player

	  
	Battleship(player_select(),player_select())"""
