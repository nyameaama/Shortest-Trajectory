import tkinter as Tkinter
from tkinter import *

#Tkinter init
root = Tk()
my_entry = Entry(root)

#Initialise canvas for simulation
simul = Tkinter.Canvas(root, bg = "black", height = 600, width = 500)
simul.pack()

def display():
    print(my_entry.get())
 
def quit_window():
    root.destroy()
    sys.exit()

#Function to initialise all window buttons
def init_buttons():
    my_button = Button(root, text = "Begin", command = display, width = 10)
    my_button.pack(pady = 10)
    my_button.place(x = 800, y = 200)
    my_button2 = Button(root, text = "Quit", command = quit_window, width = 10)
    my_button2.pack(pady = 10)
    my_button2.place(x = 800,y = 300)

#Function to initialise labels and entrys
def init_labels():
    my_label = Label(root, text = "Shortest Trajectory")
    my_label.pack(pady = 10)
    my_label.place(x = 800, y = 50)
    my_entry.pack(pady = 20)
    my_entry.place(x = 800,y = 100)


#_MAIN_
def interface_main():
    root.geometry('1000x600')
    init_labels()
    init_buttons()
    root.resizable(False, False)
    root.mainloop()

interface_main()