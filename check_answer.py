""" Written by Joseph Surrey 08/05/2023
"""

from update_score import update_score


def check_answer(questions, answer, user_answer):
    # if the users answer is the same as the answer then update the score
    if answer == user_answer:
        update_score(questions, "correct")
    # if the users answer is not the same as the answer then update the score
    else:
        update_score(questions, "incorrect")

