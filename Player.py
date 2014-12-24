#
#Darrel Jiang
#Professor Clair
#CSCI 150 MTWF(9:00-9:50am)
#
#Creates a player class for the game of battleship.
#


from Board import *
from random import *
from GraphicsManager import *

class Player():
	def __init__(self):
		"""Creates a player with 2 boards and a list of their ships"""
		self._boardShips = Board()
		self._boardShots = Board()
		
		AC = ('Aircraft Carrier', 5,)
		B = ('Battleship', 4)
		S = ('Submarine', 3)
		D = ('Destroyer', 3)
		P = ('Patrol Boat', 1)
		self._ships = (AC,B,S,D,P)

        def getShipBoard(self):
		"""returns the Ships Board"""
		return self._boardShips
		
	def getShotBoard(self):
		"""returns the Shots Board"""
		return self._boardShots
		
class HumanPlayer(Player):
	
        def placeShips(self,graphics):
		"""Allows the placement of ships at legal spaces on the battleship game board"""
		
		for ship in self._ships:
			legal = False
			size = ship[1]
			while not legal:
				(x,y) = graphics.getClickedSquare()
				(oriX,oriY) = graphics.getClickedSquare()
				
				if (oriX,oriY) == (x,y):
					print 'Choose a valid orientation'
					continue
				
				#Determines orientation by the direction of the second click
				if oriX > x:
				  ori = 'right'
				if oriX < x:
				  ori = 'left'
				if oriY > y:
				  ori = 'down'
				if oriY < y:
				  ori = 'up'
				
				if self._boardShips.isOffBoard(x,y,ori,size):
				  print 'Ship is off the board, choose a valid position for your '+ship[0]
				  continue
				if self._boardShips.isLineOccupied(x,y,ori,size):
				  print 'Position is already occupied, choose a valid position for your ' +ship[0]
				  continue
				 
				legal = True
			self._boardShips.setSquare(x,y,ori,size,graphics,ship[0][0],1)
			
	
	def fire(self,shBoard,stBoard,gShips,gShots,gOppShips):
		"""Checks if the chosen position is a valid firing position, then checks if it is a hit or a miss on a ship."""
		legal = False
		while not legal:
			(x,y) = gShots.getClickedSquare()
			
			
			if shBoard.isOccupied(x,y):
				shBoard.fireHit(x,y,gShips,1)
				stBoard.fireHit(x,y,gShots,1)
				
				legal = True
				
			if stBoard.isHitMarked(x,y):
				continue
			      
			if stBoard.isMarked(x,y):
				continue
			
			if not shBoard.isOccupied(x,y):
				stBoard.fireMiss(x,y,gShots,1)
				gOppShips.displayItem(x,y,'Miss')
				legal = True
		
			
class ComputerPlayer(Player):
  
	def placeShips(self,graphics):
		"""Allows the placement of ships at legal spaces on the battleship game board"""
		oriList = ['up','down','left','right']
		for ship in self._ships:
			legal = False
			size = ship[1]
			while not legal:
				x = randint(0,9)
				y = randint(0,9)
				randOri = randint(0,3)
				      
				ori = oriList[randOri]

				if self._boardShips.isOffBoard(x,y,ori,size):
					continue
				
				if self._boardShips.isLineOccupied(x,y,ori,size):
					continue
				      
				
				legal = True
			self._boardShips.setSquare(x,y,ori,size,graphics,ship[0][0],0)
	
	def fire(self,shBoard,stBoard,gShips,gShots,gOppShips):
		"""Checks if the chosen position is a valid firing position, then checks if it is a hit or a miss on a ship."""
		
		legal = False
		while not legal:
			x = randint(0,9)
			y = randint(0,9)
			
			if shBoard.isOccupied(x,y):
				shBoard.fireHit(x,y,gShips,1)
				stBoard.fireHit(x,y,gShots,1)
				
				legal = True
			
			if stBoard.isHitMarked(x,y):
				continue
			
			if stBoard.isMarked(x,y):
				continue
			if not shBoard.isOccupied(x,y):
				stBoard.fireMiss(x,y,gShots,0)
				gOppShips.displayItem(x,y,'Miss')
				legal = True
			
if __name__ == '__main__':
	gman = GraphicsManager()
	gman1 = GraphicsManager()
	gman2 = GraphicsManager()
	gman3 = GraphicsManager()
	p = HumanPlayer()
	p.placeShips(gman)
	p1 = ComputerPlayer()
	p1.placeShips(gman2)
	
	for x in range(20):
	  p.fire(p1.getShipBoard(),p.getShotBoard(),gman2,gman1)
	#gman.displayMove(5,5,'S')

	
