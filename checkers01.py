#Checkers By APG

from graphics import*

#square V.
s = 60

#window
win = GraphWin("Checkers",s*10 , s*10)
win.setCoords(0, 0, s*10,s*10 )

#argument for R & C
def run_S (c,r):
    Sa = Rectangle(Point(s*(r+1),s*(c+1)), Point(s*(r+2),s*(c+2)))
    Sa = ("red")
    Sa.draw(win)

#the part that calls it to action

for C in range (8):
    for R in range(8):
        if ( C+1 * R) % 2 == 0:
            run_S(R,C)
