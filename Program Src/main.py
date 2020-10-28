from Draw import *
from graphics import *
import tkinter as Tkinter
import time

#Draw Window
win = GraphWin("Shortest Trajectory", 1000, 700)

def getPoints():
    #print(midptellipse(10,15,100,100))
    print(5)

def loadImages():
    earth = Image(Point(500,500),"/Users/nyameaama/Documents/Shortest-Trajectory/assets/MarsX.gif")
    earth.draw(win)

def APP_SETUP():
    print("Setup")


def APP_LOOP():
    print("loop")
    loadImages()
    #c = Circle(Point(50,50), 1)
    #c.draw(win)
    getPoints()
    for i in range(1,600):
        win.plot(i,i)
        #time.sleep(0)

    win.getMouse() # pause for click in window win.close()
    update(60)


def main():
   APP_SETUP()
   APP_LOOP()
   #top = Tkinter.Tk()
   #B = Tkinter.Button(top, text ="Hello", command = getPoints)
   #B.pack()


main()