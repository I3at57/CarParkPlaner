"""
This files contain all the displays variables and functions.
"""

# --- Import ---
from tkinter import *
from random import randrange

# --- Constant delcare ---

PANTEXTSIZE = 100
PANTEXTCOLOR = 'white'
PANCOLOR = 'red'
BUTTONCOLOR = 'orange'
BUTTONTEXTCOLOR = 'black'


# --- Functions declare ---
def clickHelp():

    fenHelp = Tk()
    labHelp = Label(fenHelp, text="""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    You need some help ?


    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """, fg=PANTEXTCOLOR, background='red', font=PANTEXTSIZE)
    labHelp.pack()
    boutQuit = Button(fenHelp, text='Quit', fg=BUTTONTEXTCOLOR, background=BUTTONCOLOR, command = fenHelp.destroy)
    boutQuit.pack(side=RIGHT)

    labHelp.mainloop()

def reserve_place():
    nbr = randrange(100)

    fenRes = Tk()
    labRes = Label(fenRes, text="""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    The place {} is reserved for you !


    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """.format(nbr), fg=PANTEXTCOLOR, background='red', font=PANTEXTSIZE)
    labRes.pack()
    boutQuit = Button(fenRes, text='Quit', fg=BUTTONTEXTCOLOR, background=BUTTONCOLOR, command = fenRes.destroy)
    boutQuit.pack(side=RIGHT)

    fenRes.mainloop()

# --- All the windows declare ---
fenMenu1 = Tk()

# --- Label declare ---
labWelc = Label(fenMenu1, text="""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Car Park Planer


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""", fg=PANTEXTCOLOR, background=PANCOLOR, font=PANTEXTSIZE)

# Button declare
boutQuit = Button(
    fenMenu1, text='Quit', fg=BUTTONTEXTCOLOR, background=BUTTONCOLOR, command = fenMenu1.destroy
)
boutHelp = Button(fenMenu1, text='Help', fg=BUTTONTEXTCOLOR, background=BUTTONCOLOR, command = clickHelp)
boutReserved = Button(fenMenu1, text='Find a place', fg=BUTTONTEXTCOLOR, background=BUTTONCOLOR, command = reserve_place)

###############################################################################

if __name__ == '__main__':
    labWelc.pack()
    boutQuit.pack(side=RIGHT)
    boutHelp.pack(side=RIGHT)
    boutReserved.pack(side=LEFT)
    fenMenu1.mainloop()
