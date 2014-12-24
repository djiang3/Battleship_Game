#
#Darrel Jiang
#Professor Clair
#CSCI 150 MTWF(9:00-9:50am)
#
#Creates a board class for the game of battleship.
#

from GraphicsManager import *

class Board():
	"""Creates a battleship board."""
	def __init__(self, size = 10):
		"""Create a size X size board filled with '-' (hyphens)."""
		self._size = size
		self._board = list()
		
		#Initializes a list with the first letter of each ship
		self._shipList = ['A','B','S','D','P']
		
		#Creates a text based board (list of lists)
		for row in range(self._size):
			self._board.append(['-']*self._size)
			
	def getSize(self):
		"""Return size of the board."""
		return self._size

	def setSquare(self,x,y,ori,size,graphics,value,on=1):
		"""Store value at position (row, column)"""
		
		#The on variable is used to specify if a certain action should be shown on graphics, 1 represents on and any other integer represents off
		
		self._board[x][y] = value
		if on ==1:
			graphics.displayShip(x,y,value)
		
	       	if ori == 'up':
			for r in range(size):
				self._board[x][y-r] = value
				if on ==1:
					graphics.displayShip(x,y-r,value)
		if ori == 'down':
	       		for r in range(size):
				self._board[x][y+r] = value
				if on ==1:
					graphics.displayShip(x,y+r,value)
		if ori == 'left':
	       		for r in range(size):
       				self._board[x-r][y] = value
       				if on ==1:
					graphics.displayShip(x-r,y,value)
		if ori == 'right':
	       		for r in range(size):
       				self._board[x+r][y] = value
       				if on ==1:
					graphics.displayShip(x+r,y,value)
		
	def getSquare(self,x,y):
		"""Get value at postion (row,column)"""
		return self._board[x][y]
	
	def isOccupied(self,x,y):
		"""Return True if position (x,y) is occupied."""
		return self._board[x][y] in self._shipList 
	
	def isSunk(self,i):
		"""Returns True if a ship is no longer on the board"""
		cnt=0
		for x in range(self._size):
			for y in range(self._size):
				if self._board[x][y] == self._shipList[i]:
					cnt +=1
		return cnt == 0
	
	def isHitMarked(self,x,y):
		"""Determines whether or not a position has already been marked by a 'hit'."""
		return self._board[x][y] == 'X'
	
	def isMarked(self,x,y):
		"""Determines whether or not a postion has already been marked by a 'miss'."""
		return self._board[x][y] == 'O'
		
	def lostGame(self):
		"""Determines if the specified board indicates a loss."""
		sLeft = 0
		for x in range(self._size):
			for y in range(self._size):
				if self._board[x][y] in self._shipList:
					sLeft += 1
			#cnt+=1
		return sLeft == 0
		
	def fireHit(self,x,y,graphics,on=1):
		"""Replaces a coordinate with an 'X'."""
		self._board[x][y] = 'X'
		if on ==1:
			graphics.displayItem(x,y,'Hit')
	
	def fireMiss(self,x,y,graphics,on=1):
		"""Replaces a coordinate with an 'O'."""
		self._board[x][y] = 'O'
		if on ==1:
			graphics.displayItem(x,y,'Miss')
		
	def isLineOccupied(self,x,y,ori,size):
		"""Checks if the placement of an object interferes with other objects on the board."""
	  
		if self._board[x][y] != '-':
			#print 'True'
			return self._board[x][y] != '-'
		if ori == 'up':
			for r in range(size):
				if self._board[x][y-r] != '-':
					#print 'True'
					return self._board[x][y-r] != '-'
		if ori == 'down':
			for r in range(size):
				if self._board[x][y+r] != '-':
					#print 'True'
					return self._board[x][y+r] != '-'
					
		if ori == 'left':
			for r in range(size):
				if self._board[x-r][y] != '-':
					#print'True'
					return self._board[x-r][y] != '-'
					
		if ori == 'right':
			for r in range(size):
				if self._board[x+r][y] != '-':
					#print 'True'
					return self._board[x+r][y] != '-'

	def isOffBoard(self,x,y,ori,size):
		"""Checks if the placement of an object will be off the game board"""
		
		if ori == 'up':
			return ( y - (size-1)) < 0
			
		if ori == 'down':
			return ( y + (size-1) ) > 9
			
		if ori == 'left':
			return ( x - (size-1)) < 0
			
		if ori == 'right':
			return (x + (size-1)) > 9

	def __str__(self):
		"""Convert to a printable, multi-line string"""
		out = ''
		for y in range(self._size):
			for x in range(self._size):
				out += self.getSquare(x,y)	
			out += '\n'
		return out
		
if __name__ == '__main__':
	b = Board()
	#b.setSquare(4,2,'right',4)
	#b.isLineOccupied(2,5,'down',5)
	b.setSquare(5,5,'up',3)
	b.fireHit(5,5)
	b.fireHit(5,4)
	b.fireHit(5,3)
	#b.isOffBoard(5,2,'up',4)
	b.lostGame()
	print b
