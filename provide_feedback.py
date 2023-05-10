""" Written by Joseph Surrey 10/05/2023
"""

from check_for_questions import check_for_questions


def provide_feedback(questions, result, score):
    # print whether the user was correct or incorrect, and capitalize it
    print(f"{result.capitalize()}")
    # print users score
    print(f"Score: {score}")
    check_for_questions(questions, score)
