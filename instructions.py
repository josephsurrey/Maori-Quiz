""" Written by Joseph Surrey 08/05/2023
"""

from setup import *
from quiz_selection import quiz_selection


def instructions():
    print(SECTION_SEPARATOR)
    # print instructions
    print(INSTRUCTIONS.read())
    # run quiz selection
    quiz_selection()
