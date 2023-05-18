""" Written by Joseph Surrey 10/05/2023
"""

from get_valid_input import get_valid_input


def quit(score):
    # thank user for playing
    print("Thanks for playing Maori Quiz")
    # print user score
    print(f"Your score was: {score}")
    # check if user wants to play again
    play_again = get_valid_input("Would you like to play Maori Quiz again? ", str, ["YES", "Y", "NO", "N"], True)
    # if yes, go to quiz selection
    if play_again == "YES" or play_again == "Y":
        from quiz_selection import quiz_selection
        quiz_selection()
