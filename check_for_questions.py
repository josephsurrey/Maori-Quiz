""" Written by Joseph Surrey 10/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""

from quit import quit


def check_for_questions(questions, score, quiz):
    # if there are questions left in the questions list, ask another question
    if len(questions) != 0:
        from ask_question import ask_question
        ask_question(questions, score, quiz)
    # otherwise quit
    else:
        quit(score, quiz)

