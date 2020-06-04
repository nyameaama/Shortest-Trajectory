from Draw import *
from graphics import *

def main():
    win = GraphWin("Shortest Trajec", 500, 500)
    c = Circle(Point(50,50), 1)
    c.draw(win)
    win.getMouse() # pause for click in window win.close()

main()