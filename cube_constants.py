from functools import reduce

from markup import embolden, italicize

HANDS_OP = "!hands"
JUMBLE_OP = "!jumble"
SOLVE_OP = "!solve"
CUSTOM_OP = "!custom"
TEXT_OP = "!text"
HELP_OP = "!rubik"

SQUARES_IN_A_ROW = 3
SQUARES_IN_A_COLUMN = 3
SQUARES_ON_A_SIDE = SQUARES_IN_A_ROW * SQUARES_IN_A_COLUMN
SIDES = "LUFDRB"
SIDES_ON_A_CUBE = len(SIDES)
SQUARES_ON_A_CUBE = SQUARES_ON_A_SIDE * SIDES_ON_A_CUBE

COLOUR_DECODE = {
    "r": "red",
    "o": "orange",
    "y": "yellow",
    "g": "green",
    "b": "blue",
    "w": "white",
}
COLOUR_CODES = list(COLOUR_DECODE.keys())

BASIC_MOVES = ["F", "R", "U", "L", "B", "D", "M", "E", "S", "x", "y", "z"]
ALL_MOVES = reduce((lambda x, y: x + [y, y + "2", y + "'"]), BASIC_MOVES, [])
ALL_MOVES_BOLD = str(list(map((lambda x: embolden(x)), ALL_MOVES)))

ORIGINAL_IMAGE = "idle.jpg"
GRAFFITIED_IMAGE = "idle_graffitied.jpg"

HANDS_HELP = (
    "performs the moves affixed to it, e.g. "
    + italicize(HANDS_OP + " R F2 x R'")
    + " will rotate the right face 90° clockwise,"
    " rotate the front face 180° clockwise,"
    " revolve the cube on it's x axis 90°"
    " then rotate the right face 90° counterclockwise."
)
JUMBLE_HELP = "jumbles the cube."
SOLVE_HELP = "solves the cube."
CUSTOM_HELP = (
    "configures the cube with a valid string of "
    + str(SQUARES_ON_A_CUBE)
    + " colour characters."
)
TEXT_HELP = "displays the current cube configuration in text format."

COMMAND_PAIRS = {
    (HANDS_OP, HANDS_HELP),
    (JUMBLE_OP, JUMBLE_HELP),
    (SOLVE_OP, SOLVE_HELP),
    (TEXT_OP, TEXT_HELP),
    (CUSTOM_OP, CUSTOM_HELP),
}
COMMANDS_INFO = ""
for x, y in COMMAND_PAIRS:
    COMMANDS_INFO += embolden(x) + " " + y + "\n"

MOVES_INFO = (
    "Here is the list of all available moves: "
    + ALL_MOVES_BOLD
    + ". For more information about the "
    "standard rubik's cube notation, follow this link: "
    "<https://ruwix.com/the-rubiks-cube/notation/>"
)

EXAMPLE_CONFIG = "rrrbbbrrryyyyyyyyygggrrrgggwwwwwwwwwooogggooobbbooobbb"
CONFIG_INFO = (
    "An example of a valid custom configuration would be "
    + italicize(EXAMPLE_CONFIG)
    + " which defines a cube after an "
    "equator slice."
)

HELP_TEXT = COMMANDS_INFO + "\n" + MOVES_INFO + "\n\n" + CONFIG_INFO
