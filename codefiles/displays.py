"""
This files contain all the displays variables and functions.
"""

###############################################################################


# --- Import ---
from tkinter import *
from constantes import *
from random import randrange    # Only as test can be removed

# --- Variable for the navigate option ---
compt = 0
fenCurrent = MENU
fenPrevious = None

###############################################################################


# --- All the windows declare ---
window = Tk()


# --- Label Menu declare ---
labWelcMenu = Label(
    window, text=LABEL_MENU_WINDOW, fg=PANEL_TEXT_COLOR,
    background=PANEL_COLOR, font=PANEL_TEXT_SIZE
)


# --- Button Menu declare ---
boutQuitMenu = Button(
    window,
    text=QUIT_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=window.destroy
)
boutReservedMenu = Button(
    window,
    text=FIND_PLACE_MENU_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: [pack_all(MENU, bol=False), pack_all(RESV)]
)
boutSeePlacesMenu = Button(
    window,
    text=AVAIBILITY_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: [pack_all(MENU, bol=False), pack_all(AVAI)]
)


# --- Button static declare ---
boutMenuStatic = Button(
    window,
    text=MENU_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: [pack_all(fenCurrent, bol=False), pack_all(MENU)]
)
boutReturnStatic = Button(
    window,
    text=RETURN_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: [
        print(fenCurrent), print(fenPrevious),
        pack_all(fenCurrent, bol=False), pack_all(fenPrevious),
    ]
)
boutHelp = Button(
    window,
    text=HELP_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: [pack_all(fenCurrent, bol=False), pack_all(HELP)]
)


# --- Button Navigate declare ---
boutGo1 = Button(
    window,
    text=' 1 ', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: navigate(-1)
)
boutMoins10 = Button(
    window,
    text='<<<', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: navigate(0)
)
boutMoins1 = Button(
    window,
    text=' < ', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: navigate(1)
)
boutPlus1 = Button(
    window,
    text=' > ', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: navigate(2)
)
boutPlus10 = Button(
    window,
    text='>>>', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: navigate(3)
)
boutGo100 = Button(
    window,
    text='100', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command=lambda: navigate(4)
)

# --- Label declare ---
labHelp = Label(
    window,
    text=LABEL_HELP_WINDOW, fg=PANEL_TEXT_COLOR,
    background=PANEL_COLOR, font=PANEL_TEXT_SIZE
)
labResv = Label(
    window,
    text=LABEL_RESERVED_WINDOW.format(randrange(100)),
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=PANEL_TEXT_SIZE
)

textVarAvai = StringVar()
textVarAvai.set(LABEL_AVAI_WINDOW.format(compt+1, SITUATION_TAB[randrange(2)]))
labAvai = Label(
    window,
    textvariable=textVarAvai,
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=PANEL_TEXT_SIZE
)

###############################################################################


# --- Functions pack declare ---
def pack_all(win, bol=True):

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
            labWelcMenu.pack()
            boutQuitMenu.pack(side=RIGHT)
            boutHelp.pack(side=RIGHT)
            boutReservedMenu.pack(side=LEFT)
            boutSeePlacesMenu.pack(side=LEFT)
            fenCurrent = MENU
        else:
            labWelcMenu.pack_forget()
            boutQuitMenu.pack_forget()
            boutHelp.pack_forget()
            boutReservedMenu.pack_forget()
            boutSeePlacesMenu.pack_forget()
    elif win == HELP:
        if bol:
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
            # fenPrevious = fenCurrent
    elif win == RESV:
        if bol:
            labResv.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious is not None:
                boutReturnStatic.pack(side=RIGHT)
            boutHelp.pack(side=RIGHT)
            fenCurrent = RESV
        else:
            labResv.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
    elif win == AVAI:
        if bol:
            labAvai.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious is not None:
                boutReturnStatic.pack(side=RIGHT)
            boutHelp.pack(side=RIGHT)
            boutGo1.pack(side=LEFT)
            boutMoins10.pack(side=LEFT)
            boutMoins1.pack(side=LEFT)
            boutPlus1.pack(side=LEFT)
            boutPlus10.pack(side=LEFT)
            boutGo100.pack(side=LEFT)
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


# --- Functions navigate declare ---
def navigate(id):

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
    else:
        compt = 99
    print(compt+1)

    textVarAvai.set(
        LABEL_AVAI_WINDOW.format(compt+1, SITUATION_TAB[randrange(2)])
    )

    pack_all(AVAI)

###############################################################################


if __name__ == '__main__':
    pack_all(fenCurrent)
    window.mainloop()
