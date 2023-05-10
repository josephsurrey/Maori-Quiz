""" Written by Joseph Surrey 08/05/2023
"""
from ask_question import ask_question
from get_valid_input import get_valid_input
from questions import *


def quiz_selection():
    # ask user what quiz they would like to do
    quiz = get_valid_input("Please select a quiz:\n"
                           "1) Maori numbers 1-10\n"
                           "2) Maori months of the year\n"
                           "3) Maori days of the week\n"
                           "PLease enter a number between 1 and 3 to select quiz: ", int, [1, 2, 3])
    # set question list from questions file depending on what quiz the user selected
    if quiz == 1:
        questions = MAORI_NUMBERS
    elif quiz == 2:
        questions = MAORI_MONTHS
    else:
        questions = MAORI_DAYS
    # ask first question
    ask_question(questions, 0)
