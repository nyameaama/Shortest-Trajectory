import tkinter as Tkinter
from tkinter import *

#Tkinter init
root = Tk()

#Text Box init
PL1_entry = Entry(root)
PL2_entry = Entry(root)

#Initialise canvas for simulation
simul = Tkinter.Canvas(root, bg = "black", height = 600, width = 500)
simul.pack()

def display():
    print(PL1_entry.get())
 
def quit_window():
    root.destroy()
    sys.exit()

#Function to initialise all window buttons
def init_buttons():
    Run = Button(root, text = "Run", command = display, width = 10)
    Run.pack(pady = 10)
    Run.place(x = 850, y = 150)
    my_button2 = Button(root, text = "Developer Information", command = menus_, width = 10)
    my_button2.pack(pady = 10)
    my_button2.place(x = 800,y = 500)

#Function to initialise labels and entrys
def init_labels():
    title_prSection = Label(root, text = "Shortest Trajectory",font = 'Helvetica 18 bold')
    title_prSection.pack(pady = 10)
    title_prSection.place(x = 790, y = 20)

    PL1_prSection = Label(root, text = "Planet 1")
    PL1_prSection.pack(pady = 10)
    PL1_prSection.place(x = 790, y = 50)

    PL1_entry.pack(pady = 10)
    PL1_entry.place(x = 800,y = 100, height = 30, width = 50)

    PL2_prSection = Label(root, text = "Planet 2")
    PL2_prSection.pack(pady = 10)
    PL2_prSection.place(x = 920, y = 50)

    PL2_entry.pack(pady = 10)
    PL2_entry.place(x = 900,y = 100, height = 30, width = 50)
   
def init_dropdowns():
    Items = ["Mars","Earth","Jupiter","Uranus","Venus","Neptune","Saturn"]
    click = StringVar(root)
    click.set("Planet") # default value
    opMenu = OptionMenu(root,click,*Items)
    opMenu.pack()
    

def menus_():
    # create a menu
    popup = Menu(root, tearoff=0)
    root.title("Deveoper Information")
    Information = Label(root,bg = "black")
    Information.config(text = "Author - Nyameaama Gambrah")
    

#_MAIN_
def interface_main():
    root.geometry('1000x600')
    init_labels()
    init_buttons()
    init_dropdowns()
    menus_()
    root.resizable(False, False)
    root.mainloop()

interface_main()