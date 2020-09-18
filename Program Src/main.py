from Draw import *
from graphics import *
import time

def getPoints():
    points = []
    points = midptellipse(10,15,100,100)


def APP_LOOP():
    win = GraphWin("Shortest Trajectory", 1000, 700)
    #c = Circle(Point(50,50), 1)
    #c.draw(win)
    for i in range(1,600):
        win.plot(i,i)
        time.sleep(0.05)

    win.getMouse() # pause for click in window win.close()
    update(60)


def main():
   APP_LOOP()

main()