""" Written by Joseph Surrey 08/05/2023
Updated 18/05/2023 to add a method of seeing what quiz the user played
"""
import copy
import random
from get_valid_input import get_valid_input
from check_answer import check_answer
from questions import *


def ask_question(questions, score, quiz):
    # select a random question from the questions variable
    question, answer = random.choice(questions)
    # remove that question from the questions pool
    questions.remove([question, answer])
    # add the correct answer to the list of options for the question
    options = [answer]
    # run loop to add random options until options has 4 variables inside it
    while len(options) != 4:
        # select a random answer that isn't the correct one from the questions that are in the quiz the user is taking
        if quiz == "Maori Numbers":
            new_option = MAORI_NUMBERS[random.randint(0, len(MAORI_NUMBERS) - 1)][1]
        elif quiz == "Maori Months":
            new_option = MAORI_MONTHS[random.randint(0, len(MAORI_MONTHS) - 1)][1]
        elif quiz == "Maori Days":
            new_option = MAORI_DAYS[random.randint(0, len(MAORI_DAYS) - 1)][1]
        # if this is not in the list then append it to options
        if new_option not in options: # noqa
            options.append(new_option)
    # shuffle the options
    random.shuffle(options)
    """ask question, then use ord() to return an integer that represents a unicode character, then subtract 65, which
    will turn A into 0, B to 1 and so on. This allows us to represent the users input as an integer"""
    user_input = ord(get_valid_input(f"{question} (Enter a, b, c, or d)\n"
                                     f"a) {options[0]}\n"
                                     f"b) {options[1]}\n"
                                     f"c) {options[2]}\n"
                                     f"d) {options[3]}\n", str, ["A", "B", "C", "D"], True)) - 65
    # set the value of user_answer to the answer that the user chose
    user_answer = options[user_input]
    # check answer
    check_answer(questions, answer, user_answer, score, quiz)
