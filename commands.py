import pycuber as pc
from pycuber.solver import CFOPSolver
from functools import reduce

from art import draw
from db import delete_cube, append_movements_to_cube
from markup import embolden, italicize
from cube_constants import (
    ALL_MOVES,
    ALL_MOVES_BOLD,
    SIDES,
    SQUARES_ON_A_CUBE,
    COLOUR_CODES,
    COLOUR_DECODE,
    SIDES_ON_A_CUBE,
    SQUARES_IN_A_ROW,
    SQUARES_IN_A_COLUMN,
)


def hands_validate(movements):
    """Checks that a list contains only valid movements."""
    if len(movements) == 0:
        return True, None
    elif not movements[0] in ALL_MOVES:
        return (
            False,
            (
                embolden(movements[0]) + " is not a valid movement. "
                "Please use a move from this list: " + ALL_MOVES_BOLD
            ),
        )
    else:
        return hands_validate(movements[1:])


def hands(channel_id, movements):
    """Performs a valid sequence of movements on a cube."""
    valid, report = hands_validate(movements.split())
    if not valid:
        return report
    modify_and_draw_cube(channel_id, movements)


def jumble(channel_id):
    """Jumbles a cube."""
    modify_and_draw_cube(channel_id, str(pc.Formula().random()))


def solve(channel_id):
    """Solves a cube."""
    delete_cube(channel_id)
    draw(pc.Cube())


def custom(channel_id, letters):
    """	Verifies and configures a cube with a sequence of characters."""
    if len(letters) != SQUARES_ON_A_CUBE:
        return (
            "You must provide "
            + str(SQUARES_ON_A_CUBE)
            + " colour characters but you have given "
            + str(len(letters))
            + "."
        )
    for x in range(0, SQUARES_ON_A_CUBE):
        if not letters[x] in COLOUR_CODES:
            return embolden(
                letters[x]
            ) + " is not a valid colour code. " "Please only use codes from this list: " + str(
                COLOUR_CODES
            )
    colours = list(map((lambda x: COLOUR_DECODE[x]), letters))
    mycube = pc.Cube(pc.array_to_cubies(colours))
    solver = CFOPSolver(mycube)
    try:
        solution = solver.solve()
    except ValueError:
        return "You have input an impossible cube configuration."
    state = str(solution.reverse())
    delete_cube(channel_id)
    modify_and_draw_cube(channel_id, state)


def text(channel_id):
    """Returns the configuration of a cube in text form."""
    progress = append_movements_to_cube(channel_id, "")
    mycube = pc.Cube()
    mycube(progress)
    txt = ""
    for i in range(0, SIDES_ON_A_CUBE):
        for j in range(0, SQUARES_IN_A_ROW):
            for k in range(0, SQUARES_IN_A_COLUMN):
                txt += str(mycube.get_face(SIDES[i])[j][k].colour[0])
    return txt


def modify_and_draw_cube(channel_id, movements):
    """Modifies the state of a cube, creates a cube if none pre-exists."""
    progress = append_movements_to_cube(channel_id, movements)
    mycube = pc.Cube()
    mycube(progress)
    draw(mycube)
