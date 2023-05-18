""" Written by Joseph Surrey 08/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""

from update_score import update_score


def check_answer(questions, answer, user_answer, score, quiz):
    # if the users answer is the same as the answer then update the score
    if answer == user_answer:
        update_score(questions, "correct", score, quiz)
    # if the users answer is not the same as the answer then update the score
    else:
        update_score(questions, "incorrect", score, quiz)

