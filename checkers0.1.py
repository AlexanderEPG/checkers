#Checkers By APG

from graphics import*
#square V.
s = 60

#window
win = GraphWin("Checkers",s*10 , s*10)
win.setCoords(0, 0, s*10,s*10 )

#test for rectangles for checkers
##bottom left
bL = Rectangle(Point(s,s), Point(s+s,s+s))
bL.setFill("red")
bL.draw(win)


