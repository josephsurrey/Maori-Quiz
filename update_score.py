""" Written by Joseph Surrey 10/05/2023
"""

from provide_feedback import provide_feedback


def update_score(questions, result, score):
    # if user gets question correct, increase score by 1
    if result == "correct":
        score += 1
    provide_feedback(questions, result, score)
