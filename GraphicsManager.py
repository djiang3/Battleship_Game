#
#Darrel Jiang
#Professor Clair
#CSCI 150 MTWF(9:00-9:50am)
#
#Creates the graphics manager for the game of battleship
#
#

from cs1graphics import *
from SelectionList import *

class GraphicsManager:
      def __init__(self,color='skyBlue', size = 10,menu=0):
	"""Creates a graphical interface of the game board"""
        self._size = size
        if menu == 1:	#Used for creating the menu screen
		self._width = 600
        else:		#Used for the game board
		self._width = 310
        self._squareSide = self._width/float(self._size)

        self._canvas = Canvas(self._width, self._width,'skyBlue',title="Battleship")
        self._canvas.setBackgroundColor(color)
        
        #Creates the grid on the GUI
        s = 0
        for i in range(self._size - 1):
            s += self._squareSide
            self._canvas.add(Path(Point(s,0),Point(s,self._width)))
            self._canvas.add(Path(Point(0,s),Point(self._width,s)))
            
      def returnBoard(self):
	"""Used to return the canvas of a Graphics Manager."""
	return self._canvas

      def displayResult(self,g1,g2,g3,result):
	"""Displays the result in the form of a string"""
	winBox = Layer()
	msg = Text(result)
	(tw,th) = msg.getDimensions()
	box = Rectangle(tw+50, th+50)
	box.setFillColor('yellow')
	winBox.add(box)
	winBox.add(msg)
	winBox.moveTo(self._width/2, self._width/2)
	
	#Adds the winBox to all 4 graphics
	self._canvas.add(winBox)
	g1.add(winBox)
	g2.add(winBox)
	g3.add(winBox)
	
	#Closes all 4 canvases after self._canvas is clicked
	e = self._canvas.wait()
	while e.getDescription() != 'mouse click':
		e = self._canvas.wait()
	self._canvas.close()
	g1.close()
	g2.close()
	g3.close()
	  
      def displayItem(self,x,y,kind):
	  """Displays a hit or a miss as a red or white circle, respectively."""
	
	  px = (x+0.5) * self._squareSide
	  py = (y+0.5) * self._squareSide
	  
	  #Displays a red circle if it is a hit
	  if kind == 'Hit':
		hit = Circle(12,centerPt=Point(px,py))
		hit.setFillColor('red')
		hit.setBorderWidth(5)
		self._canvas.add(hit)
		
	  #Displays a white circle if it is a miss
	  if kind == 'Miss':
		miss = Circle(12,centerPt=Point(px,py))
		miss.setFillColor('white')
		miss.setBorderWidth(5)
		self._canvas.add(miss)
	  
      def displayShip(self,x,y,shape):
	  """Displays the ships as a gray circle with a letter designating its name"""
	  px = (x+0.5) * self._squareSide
	  py = (y+0.5) * self._squareSide
	  
	  #Outline of the ship
	  ship = Circle(14,centerPt=Point(px,py))
	  ship.setFillColor('gray56')
	  ship.setBorderWidth(3)
	  self._canvas.add(ship)
	  
	  #Initial of the ship
	  shipName = Text(shape, fontsize=22, centerPt=Point(px,py))
	  shipName.setFontColor('black')
	  self._canvas.add(shipName)
	  
      def getClickedSquare(self):
	  """returns the x and y coordinate of a clicked space"""
	  e = self._canvas.wait()
	  while e.getDescription() != 'mouse click':
		  e = self._canvas.wait()
		
	  p = e.getMouseLocation()
	  x = int(p.getX()/self._squareSide)
	  y = int(p.getY()/self._squareSide)
	  return (x,y)
	
      def selectFromList(self,title,selections):
	  """Displays a selection of strings in a box of buttons and returns the number corresponding to its position, between 0 and the length of the selection of strings."""
	  return selectionList(self._canvas,title,selections)
	
	
	
if __name__ == '__main__':
	g = GraphicsManager()
	
	"""g.displayMove(0,0,'S')
	g.displayMove(0,1,'S')
	g.displayMove(0,2,'S')
	g.displayMove(1,2,'S')
	g.displayMove(2,2,'S')"""
	
	for x in range(50):
		print g.getClickedSquare()
		g.returnBoard()
	
	
