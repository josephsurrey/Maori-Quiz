""" Written by Joseph Surrey 10/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""

from check_for_questions import check_for_questions
from setup import *


def provide_feedback(questions, result, answer, score, quiz):
    print(SECTION_SEPARATOR)
    if result == "correct":
        # if user is correct, print correct
        print("Correct")
    else:
        # else, print incorrect
        print(f"Incorrect, the answer was {answer}")
    # print users score
    print(f"Score: {score}")
    check_for_questions(questions, score, quiz)
