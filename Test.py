import pytest

# from UI import *
# from Dictionary import *
from UI import Ui
import Dictionary as dictionaryClass
from Wordle import Wordle

# check if code accepts lower case characters


def test_both_empty():
    result = Ui.checkInput("sonar")
    assert(result == True)

# Checking if input word is in proper(upper) case or not


def test_upper():
    result = Ui.checkInput("SONAR")
    assert(result == True)

# TO check if given word contains only aphabets or not


def test_empty():
    result = Ui.checkInput("")
    assert(result == False)

# To check if given word contains only aphabets or not


def test_num():
    result = Ui.checkInput("12345")
    assert(result == False)

# To check if input is single word or not


def test_multiple_words():
    result = Ui.checkInput("Hello World")
    assert(result == False)

# To check if a given word was entered before or not


def test_word_used_one():
    result = Ui.checkWordUsed(
        "sonar".upper(), ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == False)


def test_word_used_two():
    result = Ui.checkWordUsed(
        "SONAR".upper(), ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == False)


def test_word_used_three():
    result = Ui.checkWordUsed(
        "SHIFT", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)


def test_word_used_four():
    result = Ui.checkWordUsed(
        "", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)

# Checking for proper length of words


def test_word_length_one():
    result = Ui.checkWordLength(
        "     ")
    assert(result == False)


def test_word_length_two():
    result = Ui.checkWordLength(
        "")
    assert(result == False)


def test_word_length_three():
    result = Ui.checkWordLength(
        "SONAR")
    assert(result == True)


def test_word_length_four():
    result = Ui.checkWordLength(
        "SON")
    assert(result == False)


def test_word_length_five():
    result = Ui.checkWordLength(
        "SONARSONARSONAR")
    assert(result == False)


def test_dict_word_length():
    todays_word, word_list = dictionaryClass.Dictionary().getRandomWord([
        "YACHT"])
    assert(len(todays_word) == 5)

# Checking if chosen word is from the provided word list


def test_word_in_dict():
    todays_word, word_list = dictionaryClass.Dictionary().getRandomWord([
        "YACHT"])
    assert(todays_word in word_list)

# Checking if dictionary module returns word in proper(upper) case or not


def test_word_dict_isUpper():
    todays_word, word_list = dictionaryClass.Dictionary().getRandomWord([
        "YACHT"])
    assert(todays_word.isupper())

# Checking if Division by zero error is being handled or not


def test_divide_by_zero():
    game = Wordle()
    assert(game.displayResults(0, 0, []) == None)
