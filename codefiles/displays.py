"""
This files contain all the displays variables and functions.
"""

###############################################################################


# --- Import ---
from tkinter import *
from random import randrange    # Only as test can be removed
RAND_NBR = randrange(100)
from constantes import *

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
    window, text='Quit', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command = window.destroy
)
boutHelpMenu = Button(
    window, text='Help', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command = lambda:[pack_all('menu', bol=False),pack_all('help')]
)
boutReservedMenu = Button(
    window, text='Find a place', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command = lambda:[pack_all('menu', bol=False),pack_all('resv')]
)

# --- Label Help declare ---
labHelp = Label(
    window, text=LABEL_HELP_WINDOW, fg=PANEL_TEXT_COLOR,
    background=PANEL_COLOR, font=PANEL_TEXT_SIZE
)

# --- Button Help declare ---
boutQuitHelp = Button(
    window, text='Quit', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command = lambda:[pack_all('help', bol=False),pack_all('menu')]
)

# --- Label Reserved declare ---
labResv = Label(
    window, text=LABEL_RESERVED_WINDOW.format(RAND_NBR),
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=PANEL_TEXT_SIZE
)

# --- Button Reserved declare ---
boutQuitResv = Button(
    window, text='Quit', fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    command = lambda:[pack_all('resv', bol=False),pack_all('menu')]
)

###############################################################################


# --- Functions declare ---
def pack_all(win, bol=True):

    if win == 'menu':
        if bol == True:
            labWelcMenu.pack()
            boutQuitMenu.pack(side=RIGHT)
            boutHelpMenu.pack(side=RIGHT)
            boutReservedMenu.pack(side=LEFT)
        else:
            labWelcMenu.pack_forget()
            boutQuitMenu.pack_forget()
            boutHelpMenu.pack_forget()
            boutReservedMenu.pack_forget()
    elif win == 'help':
        if bol == True:
            labHelp.pack()
            boutQuitHelp.pack(side=RIGHT)
        else:
            labHelp.pack_forget()
            boutQuitHelp.pack_forget()
    elif win == 'resv':
        if bol == True:
            labResv.pack()
            boutQuitResv.pack(side=RIGHT)
        else:
            labResv.pack_forget()
            boutQuitResv.pack_forget()

###############################################################################

if __name__ == '__main__':
    pack_all('menu')
    window.mainloop()
