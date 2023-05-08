""" Written by Joseph Surrey 08/05/2023
"""

from get_valid_input import get_valid_input
from quiz_selection import quiz_selection
from instructions import instructions
from setup import *


def welcome():
    # print welcome message
    print(WELCOME_MESSAGE)
    # ask if user has played before
    played_before = get_valid_input("Have you played Maori Quiz before?", str, ["YES", "Y", "NO", "N"], True)
    # if user has played before run quiz selection
    if played_before == "YES" or played_before == "Y":
        quiz_selection()
    else:
        instructions()

