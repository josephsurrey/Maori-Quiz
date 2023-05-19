""" Written by Joseph Surrey 10/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""

from provide_feedback import provide_feedback


def update_score(questions, result, answer, score, quiz):
    # if user gets question correct, increase score by 1
    if result == "correct":
        score += 1
    provide_feedback(questions, result, answer, score, quiz)
