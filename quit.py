""" Written by Joseph Surrey 10/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""

from get_valid_input import get_valid_input
from questions import *
from setup import *


def quit(score, quiz):
    print(SECTION_SEPARATOR)
    # thank user for playing
    print(f"Thanks for playing the {quiz} quiz")
    # print user score
    if quiz == "Maori Numbers":
        print(f"Your score was {score}/{len(MAORI_NUMBERS)}")
    elif quiz == "Maori Months":
        print(f"Your score was {score}/{len(MAORI_MONTHS)}")
    elif quiz == "Maori Days":
        print(f"Your score was {score}/{len(MAORI_DAYS)}")
        print(SECTION_SEPARATOR)
    # check if user wants to play again
    play_again = get_valid_input("Would you like to play Maori Quiz again? ", str, ["YES", "Y", "NO", "N"], True)
    # if yes, go to quiz selection
    if play_again == "YES" or play_again == "Y":
        from quiz_selection import quiz_selection
        quiz_selection()
