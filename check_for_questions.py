""" Written by Joseph Surrey 10/05/2023
"""

from quit import quit


def check_for_questions(questions, score):
    # if there are questions left in the questions list, ask another question
    if len(questions) != 0:
        from ask_question import ask_question
        ask_question(questions, score)
    # otherwise quit
    else:
        quit(score)
