"""
This files contain all the displays variables and functions.
"""

###############################################################################


# --- Import ---
from tkinter import *
import tkinter.font
from constantes import *

# --- Variable for the navigate option ---
compt = -1
fenCurrent = MENU
fenPrevious = None

AVAILABILITIES = []

###############################################################################


# --- All the windows declare ---
window = Tk()   # declare iteration Tk()
window.geometry(WIN_SIZE1)  # init the size and position of the window

# create the main font of the program
myFont = tkinter.font.Font(family='Helvetica', size=15)

# --- Label Menu declare ---
"""This label is used on the main menu"""
labWelcMenu = Label(
    window, text=LABEL_MENU_WINDOW, fg=PANEL_TEXT_COLOR,
    background=PANEL_COLOR, font=myFont
)


# --- Button Menu declare ---
"""This button close and delete the window. Only accesible by the menu scene"""
boutQuitMenuScene = Button(
    window,
    text=QUIT_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=window.destroy
)
"""This button lead to the navigation scene"""
boutSeePlacesScene = Button(
    window,
    text=AVAIBILITY_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [pack_all(MENU, bol=False), pack_all(AVAI)]
)
"""
This button lead to the sea all scene
This one dont pack a new scene, this is done into the see_all() function
"""
boutSeeAllScene = Button(
    window,
    text=SEE_PLACE_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [pack_all(MENU, bol=False), see_all()]
)


# --- Button static declare ---
"""
This button is packed into all scene exept the menu
This button lead to the menu scene
"""
boutMenuStatic = Button(
    window,
    text=MENU_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [pack_all(fenCurrent, bol=False), pack_all(MENU)]
)
"""
The return button allow the user to comme back at the previous scene
if the previous was not the menu
"""
boutReturnStatic = Button(
    window,
    text=RETURN_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [
        pack_all(fenCurrent, bol=False), pack_all(fenPrevious),
    ]
)
"""
Button which lead to the menu scene
"""
boutHelp = Button(
    window,
    text=HELP_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [pack_all(fenCurrent, bol=False), pack_all(HELP)]
)


# --- Button Navigate declare ---
# All the button linked to the see available scene
boutGo1 = Button(
    window,
    text=' 1 ', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: navigate(-1)
)
boutMoins10 = Button(
    window,
    text='<<<', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: navigate(0)
)
boutMoins1 = Button(
    window,
    text=' < ', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: navigate(1)
)
boutPlus1 = Button(
    window,
    text=' > ', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: navigate(2)
)
boutPlus10 = Button(
    window,
    text='>>>', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: navigate(3)
)
boutGo100 = Button(
    window,
    text='100', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: navigate(4)
)
boutReserve = Button(
    window,
    text=RESERVE_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [make_reservation(compt), navigate(-2)]
)
boutStopReserve = Button(
    window,
    text=UNRESERVE_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [make_reservation(compt, bol=False), navigate(-2)]
)

# --- Label declare ---
labHelp = Label(
    window,
    text=LABEL_HELP_WINDOW, fg=PANEL_TEXT_COLOR,
    background=PANEL_COLOR, font=myFont
)
textVarAvai = StringVar()
textVarAvai.set(LABEL_AVAI_INTRO)
labAvai = Label(
    window,
    textvariable=textVarAvai,
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=myFont
)
textVarSee = StringVar()
textVarSee.set('')
labParking = Label(
    window,
    textvariable=textVarSee,
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=myFont
)

###############################################################################


def read_file():
    """
    This function read the txt file and fil with 100 one or zero, according
    to the available places, the list AVAILABILITIES.
    """
    f = open('availabilities.txt', 'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        info = line.split(':')
        slot = int(info[0]) - 1
        available = int(info[1])
        AVAILABILITIES.insert(slot, available)
    f.close()


def make_reservation(slot, bol=True):
    """
    This function change the value of the coresponding slot in AVAILABILITIES
    depending on the value of bol
    """
    if bol:
        AVAILABILITIES[slot] = 1
    else:
        AVAILABILITIES[slot] = 0


def save_file():
    """
    This function read AVAILABILITIES and modify the .txt in consequence
    """
    f = open('availabilities.txt', 'w')
    for i in range(len(AVAILABILITIES)):
        print("%d:%d" % (i+1, AVAILABILITIES[i]), file=f)
    f.close()


def nbr_available():
    """
    Calculate how many places are currently
    available in the list AVAILABILITIES
    """
    count = 0
    for i in AVAILABILITIES:
        if i == 0:
            count += 1
    return count


# --- Functions pack declare ---
def pack_all(win, bol=True):
    """
    This function is use to pack or unpack the widget depending on
    the scene we want.
    """

    global fenCurrent
    global fenPrevious
    global compt

    if bol:
        if fenCurrent == MENU:
            fenPrevious = None
        else:
            fenPrevious = fenCurrent

    if win == MENU:
        if bol:
            window.geometry(WIN_SIZE1)
            labWelcMenu.pack()
            boutQuitMenuScene.pack(side=RIGHT)
            boutHelp.pack(side=RIGHT)
            boutSeePlacesScene.pack(side=LEFT)
            boutSeeAllScene.pack(side=LEFT)
            fenCurrent = MENU
        else:
            labWelcMenu.pack_forget()
            boutQuitMenuScene.pack_forget()
            boutHelp.pack_forget()
            boutSeePlacesScene.pack_forget()
            boutSeeAllScene.pack_forget()
    elif win == HELP:
        if bol:
            window.geometry(WIN_SIZE3)
            labHelp.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious is not None:
                boutReturnStatic.pack(side=RIGHT)
            fenCurrent = HELP
        else:
            labHelp.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
    elif win == AVAI:
        if bol:
            window.geometry(WIN_SIZE1)
            labAvai.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious is not None and fenPrevious != AVAI:
                boutReturnStatic.pack(side=RIGHT)
            if fenPrevious != HELP:
                boutHelp.pack(side=RIGHT)
            boutGo1.pack(side=LEFT)
            boutMoins10.pack(side=LEFT)
            boutMoins1.pack(side=LEFT)
            boutPlus1.pack(side=LEFT)
            boutPlus10.pack(side=LEFT)
            boutGo100.pack(side=LEFT)
            if (AVAILABILITIES[compt] == 0) and (compt != -1):
                boutReserve.pack(side=LEFT)
            elif (AVAILABILITIES[compt] == 1) and (compt != -1):
                boutStopReserve.pack(side=LEFT)
            fenCurrent = AVAI
        else:
            labAvai.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
            boutGo1.pack_forget()
            boutMoins10.pack_forget()
            boutMoins1.pack_forget()
            boutPlus1.pack_forget()
            boutPlus10.pack_forget()
            boutGo100.pack_forget()
            boutReserve.pack_forget()
            boutStopReserve.pack_forget()
    elif win == SEEA:
        if bol:
            window.geometry(WIN_SIZE2)
            labParking.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious != HELP:
                boutHelp.pack(side=RIGHT)
            if fenPrevious is not None:
                boutReturnStatic.pack(side=RIGHT)
            fenCurrent = SEEA
        else:
            labParking.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
            boutMenuStatic.pack_forget()


# --- Functions navigate declare ---
def navigate(id):
    """
    This function change the text of the label labAvai depending
    on the number of the place the user is watching.
    """

    global compt

    pack_all(AVAI, bol=False)

    if id == -1:
        compt = 0
    elif id == 0:
        if compt > 9:
            compt = compt - 10
    elif id == 1:
        if compt > 0:
            compt = compt - 1
    elif id == 2:
        if compt < 99:
            compt = compt + 1
    elif id == 3:
        if compt < 90:
            compt = compt + 10
    elif id == 4:
        compt = 99
    else:
        pass

    textVarAvai.set(
        LABEL_AVAI_WINDOW.format(compt+1, SITUATION_TAB[AVAILABILITIES[compt]])
    )

    pack_all(AVAI)


# --- Functions see all declare ---
def see_all():
    """
    This function is used to displas the 'X' or '0'
    into the scene 'See all places'
    """

    SIGNS = []
    for i in range(len(AVAILABILITIES)):
        SIGNS.append(DISPLAY_TAB[AVAILABILITIES[i]])

    textVarSee.set(LABEL_PARKING_WINDOW.format(*SIGNS, nbr_available()))

    pack_all(SEEA)

###############################################################################


if __name__ == '__main__':
    read_file()
    pack_all(fenCurrent)
    window.mainloop()
    save_file()
