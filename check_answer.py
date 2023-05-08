""" Written by Joseph Surrey 05/05/2023
"""


def check_answer(questions, answer, user_answer):
    if answer == user_answer:
        update_score(questions, "correct")
    else:
        update_score(questions, "incorrect")

