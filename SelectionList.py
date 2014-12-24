#
#Darrel Jiang
#Professor Clair
#CSCI 150 MTWF(9:00-9:50am)
#
#A selection list class that allows for the graphical user interface for selecting players, as well as showing the main menu.
#
from cs1graphics import *

def selectionList(can,title,selections,bgcolor='steelblue'):
	"""Display a menu, wait for the user to make a selection, and return
	a number from 0 to len(selections)-1 indicating the user's choice.
	Arguments are:
	   can - the Canvas to display on
	   title - a string to display above the selections
	   selections - a list of strings
	   bgcolor - the background color of the selection box
	"""
	
	hpad = 25  # space for left and right sides of a box
	vpad = 25  # space above a box
	sgap = 15  # pixel gap between selection boxes

	header = Text(title)
	gameName = Text('Battleship',120)
	gameName.setFontColor('midnightblue')
	
	#-----Instructions Body-----
	
	#Instruction Title
	instrTitle = Text('Instructions',50)
	
	#Instruction number 1
	instrBody1 = Text('1) Begin by placing the boards in the appropriate location.',15,Point(-20,380))
	instrBody1a = Text('- The Ship Board is designated as Light Blue.',15,Point(0,400))
	instrBody1b = Text('- The Shot Board is designated as Royal Blue.',15,Point(6,420))
	
	#Instruction number 2
	instrBody2 = Text('2) Place ships by clicking a point and clicking another point in the',15,Point(5,460)) 
	instrBody2a = Text('direction you want your ship to designate the orientation.',15,Point(0,480))
	
	#Instruction number 3
	instrBody3 = Text('3) Select on the Shots Board to specify firing coordinates',15,Point(-23,520))
	
	#Instruction number 4
	instrBody4 = Text("4) Sink your opponent's ships!",15,Point(-114,560))
	
	#Dimensions for the header
	(tw,th) = header.getDimensions()

	(boxw,boxh) = (can.getWidth() - 2*hpad,2*vpad + th + (sgap + th)*len(selections))
	box = Rectangle(boxw,boxh,centerPt = Point(0,vpad+3*boxh/2))
	box.setFillColor(bgcolor)
	box.setBorderWidth(4)

	header.move(0,6.5*vpad+th/2)
	gameName.move(0,2.5*vpad+th/2)
	instrTitle.move(0,13*vpad+th/2)
	
	winbox = Layer()
	winbox.add(box)
	winbox.add(header)
	winbox.add(gameName)
	
	#-----Instructions Body added to canvas------
	
	#Instructions Title
	winbox.add(instrTitle)
	
	#Instruction number 1
	winbox.add(instrBody1)
	winbox.add(instrBody1a)
	winbox.add(instrBody1b)
	
	#Instruction number 2
	winbox.add(instrBody2)
	winbox.add(instrBody2a)
	
	#Instruction number 3
	winbox.add(instrBody3)
	
	#Instruction number 4
	winbox.add(instrBody4)
	
	winbox.move(can.getWidth()/2,0)
  
	itemy = 6.7*vpad+th/2 + sgap + th
	ycenters = list()
	for item in selections:
		r = Rectangle(boxw-2*hpad,sgap/3+th,centerPt = Point(0,itemy))
		r.setFillColor('white')
		winbox.add(r)
		winbox.add(Text(item,centerPt = Point(0,itemy)))
		ycenters.append(itemy)
		itemy += sgap + th

	can.add(winbox)

	
	# Wait for a selection
	selected = -1   # no selection
	while selected == -1:
		e = can.wait()
		if e.getDescription() != 'mouse click':
			continue
		click = e.getMouseLocation()
		# Check x coordinate in range
		clickx = click.getX()
		if clickx < can.getWidth()/2 - boxw/2 + hpad:
			# too far left
			continue
		if clickx > can.getWidth()/2 + boxw/2 - hpad:
			# too far right
			continue
			
		# Base selection off of y coordinate
		clicky = click.getY()
		for i in range(len(ycenters)):
			if abs(clicky - ycenters[i]) < (sgap/3 + th)/2:
				selected = i
	
	# Got a selection, clean up and return it
	can.remove(winbox)
	return selected
		

