from canvas_functions import *
from graphics import *
from interface import *
import time

def getPoints():
    #print(midptellipse(10,15,100,100))
    print(5)

def loadImages():
    img = PhotoImage(file="/Users/nyameaama/Documents/Shortest-Trajectory/assets/MarsX.gif")      
    simul.create_image(20,20, anchor=NW, image=img)


def APP_SETUP():
    print("Setup")

'''
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
'''