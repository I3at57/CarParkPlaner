"""
This file contain all the constant in the project.
Here are decleare all variables that don't use library.
"""

###############################################################################


# --- Constant for parameters windows displaying---
PANEL_TEXT_COLOR = 'white'
PANEL_COLOR = 'blue'
BUTTON_COLOR = 'pink'
BUTTON_TEXT_COLOR = 'black'

# three different size for the window
WIN_SIZE1 = "900x392+400+200"
WIN_SIZE2 = "1270x692+0+0"
WIN_SIZE3 = "900x460+400+200"

# --- Constant for button text ---
QUIT_BUTTON = 'Quit'
HELP_BUTTON = 'Help'
MENU_BUTTON = 'Menu'
RETURN_BUTTON = 'Return'
AVAIBILITY_BUTTON = 'Avaibility'
RESERVE_BUTTON = 'Reserve'
UNRESERVE_BUTTON = 'Stop Reserving'
SEE_PLACE_BUTTON = 'See places'

# --- Constant for scene ---
MENU = 'menu'
HELP = 'help'
AVAI = 'avai'
SEEA = 'seea'

# --- Const for the place situation ---
FREE = 'free'
USE = 'used'

SITUATION_TAB = [FREE, USE]
"""
this array is used to convert a value into AVAILABILITIES (1 or 0)
into a string

for exemple SITUATION_TAB[AVAILABILITIES[45]] will takes the value 'free' or
'used' according to the situation of the place 45
"""
DISPLAY_TAB = ['0', 'X']
"""
Same principe as the previous one.
We use this list to convert a 1 or 0 into 'X' or '0'
"""

###############################################################################


LABEL_HELP_WINDOW = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Press 'Avaibiliy' to see the availability of each places and reserve it.
Use the arrows to navigate into the different places.

Press 'See places' to have a global view of the situation of each place.

Press 'Menu' to go back at the main menu of the application.

Press 'Quit' to quit the application.

Please contact the after-sales service for more informations.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

LABEL_MENU_WINDOW = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Car Park Planer

A parking manager project by Lucas Martinez and Baptiste Toussaint



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

LABEL_AVAI_WINDOW = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




The place {} is {}




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

LABEL_AVAI_INTRO = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




See the available places




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# This one is not use in the program but wee keep it just in case
LABEL_PARKING_WINDOW2 = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1	2	3	4	5	6	7	8	9	10
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

11	12	13	14	15	16	17	18	19	20
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

21	22	23	24	25	26	27	28	29	30
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

31	32	33	34	35	36	37	38	39	40
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

41	42	43	44	45	46	47	48	49	50
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

51	52	53	54	55	56	57	58	59	60
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

61	62	63	64	65	66	67	68	69	70
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

71	72	73	74	75	76	77	78	79	80
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

81	82	83	84	85	86	87	88	89	90
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

91	92	93	94	95	96	97	98	99	100
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

                                        {} slots are available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

LABEL_PARKING_WINDOW = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

16	17	18	19	20	21	22	23	24	25	26	27	28	29	30
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

31	32	33	34	35	36	37	38	39	40	41	42	43	44	45
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

46	47	48	49	50	51	52	53	54	55	56	57	58	59	60
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

61	62	63	64	65	66	67	68	69	70	71	72	73	74	75
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

76	77	78	79	80	81	82	83	84	85	86	87	88	89	90
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

91	92	93	94	95	96	97	98	99	100
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}

{} slots are available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
