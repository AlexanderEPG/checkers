#Checkers By APG

from graphics import*
#square V.
s = 60

#window
win = GraphWin("Checkers",s*10 , s*10)
win.setCoords(0, 0, s*10,s*10 )

#test for rectangles for checkers
##bottom left
r = Rectangle(Point(s,s), Point(s+s,s+s))
r.setFill("red")
r.draw(win)

b = Rectangle(Point(s+s,s), Point(s*3,s+s))
b.setFill("black")
b.draw(win)
        
for r in range(8):
    for b in range(8):
        
