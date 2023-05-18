""" Written by Joseph Surrey 10/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""

from check_for_questions import check_for_questions


def provide_feedback(questions, result, score, quiz):
    # print whether the user was correct or incorrect, and capitalize it
    print(f"{result.capitalize()}")
    # print users score
    print(f"Score: {score}")
    check_for_questions(questions, score, quiz)
