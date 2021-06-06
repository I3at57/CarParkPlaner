"""
This file contain all the tkinter object in the project.
Here are decleare all object that use library.
"""

###############################################################################

from constantes import *
from tkinter import *
import tkinter.font
import datetime

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
"""This button lead to the login scene"""
boutLogMenuScene = Button(
    window,
    text=LOG_BUTTON_SCENE, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [pack_all(fenCurrent, bol=False), pack_all(LOGI)]
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

# --- Button boutLog declare ---
boutLog = Button(
    window,
    text=LOG_BUTTON, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR,
    font=myFont,
    command=lambda: [log_in()]
)

# --- Label declare ---
# --- Label labHelp declare ---
labHelp = Label(
    window,
    text=LABEL_HELP_WINDOW, fg=PANEL_TEXT_COLOR,
    background=PANEL_COLOR, font=myFont
)

# --- Label labAvai declare ---
textVarAvai = StringVar()
textVarAvai.set(LABEL_AVAI_INTRO)
labAvai = Label(
    window,
    textvariable=textVarAvai,
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=myFont
)

# --- Label labParking declare ---
textVarSee = StringVar()
textVarSee.set('')
labParking = Label(
    window,
    textvariable=textVarSee,
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=myFont
)

# --- Label labLog declare ---
textVarLog = StringVar()
textVarLog.set(LABEL_LOG_INTRO)
labLog = Label(
    window,
    textvariable=textVarLog,
    fg=PANEL_TEXT_COLOR, background=PANEL_COLOR, font=myFont
)

# --- Entry entryLog declare ---
userName = StringVar()
entryLog = Entry(
    window, fg=BUTTON_TEXT_COLOR, background=BUTTON_COLOR, font=myFont,
    textvariable=userName
)

###############################################################################

# --- Variable for the navigate option ---
compt = -1
fenCurrent = MENU
fenPrevious = None

AVAILABILITIES = []
USER = []
nbrUser = 0
currentUser = None


# --- Functions read_file() declare ---
def read_file():
    """
    This function read the txt file and fil with 100 one or zero, according
    to the available places, the list AVAILABILITIES.
    """

    global nbrUser

    f = open('availabilities.txt', 'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        info = line.split(':')
        slot = int(info[0]) - 1
        available = int(info[1])
        AVAILABILITIES.insert(slot, available)
    f.close()

    f = open('accounts.txt', 'r')
    lines = f.readlines()

    nbrUser = int(lines[0].replace("\n", ""))

    compt = 1
    for i in range(nbrUser):
        compt = compt + 1
        guy = {
            'name': None,
            'current_reservation': None,
            'past_reservation': None,
            'current_reservation_tab': [],
            'past_reservation_tab': [],
        }
        guy['name'] = lines[compt].replace("\n", "")
        compt += 1
        guy['current_reservation'] = int(lines[compt].replace("\n", ""))
        compt += 1
        guy['past_reservation'] = int(lines[compt].replace("\n", ""))
        compt += 1
        if guy['current_reservation'] != 0:
            for j in range(guy['current_reservation']):
                info = lines[compt].replace("\n", "")
                date_begin = {
                    'day': (int(info[:2]), int(info[3:5]), int(info[6:10])),
                    'hour': (int(info[11:13]), int(info[14:16])),
                    'place': (int(info[17:]))
                }
                guy['current_reservation_tab'].append(date_begin)
                compt += 1
        if guy['past_reservation'] != 0:
            for j in range(guy['past_reservation']):
                info = lines[compt].replace("\n", "")
                date_end = {
                    'day': (int(info[:2]), int(info[3:5]), int(info[6:10])),
                    'hour': (int(info[11:13]), int(info[14:16])),
                    'place': (int(info[17:]))
                }
                guy['past_reservation_tab'].append(date_end)
                compt += 1

        USER.append(guy)
        compt = compt + 1
    f.close()


# --- Functions make_reservation() declare ---
def make_reservation(slot, bol=True):
    """
    This function change the value of the coresponding slot in AVAILABILITIES
    depending on the value of bol
    """

    global userName

    use = userName.get()

    if bol:
        AVAILABILITIES[slot] = 1
        if use is not "":
            pos = find_pos_user(use)
            date = str(datetime.datetime.now())
            date_begin = {
                'day': (date[8:10], date[5:7], date[:4]),
                'hour': (date[11:13], date[14:16]),
                'place': (str(slot))
            }
            USER[pos]['current_reservation'] \
                = USER[pos]['current_reservation'] + 1
            USER[pos]['current_reservation_tab'].append(date_begin)
        else:
            pass
    else:
        AVAILABILITIES[slot] = 0
        if use is not "":
            pos = find_pos_user(use)
            place = find_res(slot, pos)
            del USER[pos]['current_reservation_tab'][place]
            USER[pos]['current_reservation'] \
                = USER[pos]['current_reservation'] - 1
            date = str(datetime.datetime.now())
            date_begin = {
                'day': (date[8:10], date[5:7], date[:4]),
                'hour': (date[11:13], date[14:16]),
                'place': (str(slot))
            }
            USER[pos]['past_reservation'] \
                = USER[pos]['past_reservation'] + 1
            USER[pos]['past_reservation_tab'].append(date_begin)
        else:
            pass


# --- Functions save_file() declare ---
def save_file():

    global nbrUser

    """
    This function read AVAILABILITIES and modify the .txt in consequence
    """
    f = open('availabilities.txt', 'w')
    for i in range(len(AVAILABILITIES)):
        print("%d:%d" % (i+1, AVAILABILITIES[i]), file=f)
    f.close()

    f = open('accounts.txt', 'w')
    print("%d" % (nbrUser), file=f)
    for i in USER:
        print("*", file=f)
        print(i['name'], file=f)
        print(i['current_reservation'], file=f)
        print(i['past_reservation'], file=f)
        for j in i['current_reservation_tab']:
            f.write(
                "{:02d}/{:02d}/{:02d}:{:02d}h{:02d}-{}"
                .format(
                    int(j['day'][0]), int(j['day'][1]), int(j['day'][2]),
                    int(j['hour'][0]), int(j['hour'][1]), int(j['place'])
                )
            )
            f.write("\n")
        for j in i['past_reservation_tab']:
            f.write(
                "{:02d}/{:02d}/{:02d}:{:02d}h{:02d}-{}"
                .format(
                    int(j['day'][0]), int(j['day'][1]), int(j['day'][2]),
                    int(j['hour'][0]), int(j['hour'][1]), int(j['place'])
                )
            )
            f.write("\n")
        print("*", file=f)
    f.close()


# --- Functions nbr_available() declare ---
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


def find_pos_user(str):
    pos = 0
    for i in USER:
        if i['name'] == str:
            return(pos)
            break
        else:
            pos = pos + 1


def find_res(str, user):
    if user is not None:
        pos = 0
        for i in USER[user]['current_reservation_tab']:
            if i['place'] == str:
                return(pos)
                break
            else:
                pos = pos + 1


# --- Functions pack declare ---
def pack_all(win, bol=True):
    """
    This function is use to pack or unpack the widget depending on
    the scene we want.
    """

    global fenCurrent
    global fenPrevious
    global compt

    if win == MENU:
        if bol:
            window.geometry(WIN_SIZE1)
            labWelcMenu.pack()
            boutQuitMenuScene.pack(side=RIGHT)
            boutHelp.pack(side=RIGHT)
            boutLogMenuScene.pack(side=RIGHT)
            if currentUser is not None:
                boutSeePlacesScene.pack(side=LEFT)
            boutSeeAllScene.pack(side=LEFT)
            fenPrevious = None
            fenCurrent = MENU
        else:
            labWelcMenu.pack_forget()
            boutQuitMenuScene.pack_forget()
            boutHelp.pack_forget()
            boutLogMenuScene.pack_forget()
            boutSeePlacesScene.pack_forget()
            boutSeeAllScene.pack_forget()
    elif win == HELP:
        if bol:
            window.geometry(WIN_SIZE3)
            labHelp.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious is not None:
                boutReturnStatic.pack(side=RIGHT)
            if fenCurrent != HELP:
                fenPrevious = fenCurrent
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
            if fenPrevious != HELP:
                boutHelp.pack(side=RIGHT)
            if fenPrevious is not None and fenPrevious != AVAI:
                boutReturnStatic.pack(side=RIGHT)
            boutLogMenuScene.pack(side=RIGHT)
            boutGo1.pack(side=LEFT)
            boutMoins10.pack(side=LEFT)
            boutMoins1.pack(side=LEFT)
            boutPlus1.pack(side=LEFT)
            boutPlus10.pack(side=LEFT)
            boutGo100.pack(side=LEFT)
            if (AVAILABILITIES[compt] == 0) and (compt != -1):
                boutReserve.pack(side=LEFT)
            elif (AVAILABILITIES[compt] == 1) and (compt != -1):
                print(currentUser)
                print(find_res(compt, find_pos_user(currentUser)))
                if find_res(compt, find_pos_user(currentUser)) is not None:
                    boutStopReserve.pack(side=LEFT)
            if fenPrevious != AVAI:
                fenPrevious = fenCurrent
            fenCurrent = AVAI
        else:
            labAvai.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
            boutLogMenuScene.pack_forget()
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
            if fenPrevious != SEEA:
                fenPrevious = fenCurrent
            fenCurrent = SEEA
        else:
            labParking.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
            boutMenuStatic.pack_forget()
    elif win == LOGI:
        if bol:
            window.geometry(WIN_SIZE1)
            labLog.pack()
            boutMenuStatic.pack(side=RIGHT)
            if fenPrevious != HELP:
                boutHelp.pack(side=RIGHT)
            if (
                fenPrevious is not None
            ) and (fenCurrent != HELP and fenPrevious != LOGI):
                boutReturnStatic.pack(side=RIGHT)
            boutLog.pack(side=RIGHT)
            entryLog.pack(side=RIGHT)
            if fenCurrent != LOGI:
                fenPrevious = fenCurrent
            if fenCurrent != LOGI:
                fenCurrent = LOGI
        else:
            labLog.pack_forget()
            boutMenuStatic.pack_forget()
            boutReturnStatic.pack_forget()
            boutHelp.pack_forget()
            boutLog.pack_forget()
            entryLog.pack_forget()

    print(fenCurrent, fenPrevious)


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


# --- Functions log_in declare ---
def log_in():

    global nbrUser
    global currentUser

    str_username = userName.get()
    print(str_username)
    print(find_pos_user(str_username))

    if find_pos_user(str_username) is None:
        guy = {
            'name': str_username,
            'current_reservation': 0,
            'past_reservation': 0,
            'current_reservation_tab': [],
            'past_reservation_tab': [],
        }
        USER.append(guy)
        print(USER)
        nbrUser = nbrUser + 1

    currentUser = str_username

    textVarLog.set(LABEL_LOG.format(str(str_username)))

    pack_all(LOGI, bol=False)
    pack_all(LOGI)
