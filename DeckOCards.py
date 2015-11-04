__author__ = 'blarson2'

# !/usr/local/bin/python

import random
import datetime


def shuf() -> list:

    temp = []
    for i in range(77):
        temp.append(i)
    random.seed(datetime)
    return random.shuffle(temp)


# parses raw card data into a string of its properties
def parseint(deck):
    # lists for card properties
    minor = ['north has the ', 'east has the ', 'south has the ', 'west has the '], \
        ['ace ', 'deuce ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ',
         'nine ', 'ten ', 'page ', 'knight ', 'queen ', 'king '], \
        ['of wands.', 'of cups.', 'of swords.', 'of coins.', '.']

    major = ['magician.', 'priestess.', 'empress.', 'emperor.', 'hierophant.', 'lovers.', 'chariot.',
             '\b\b\b\bstrength.', 'hermit.', '\b\b\b\bfortune.', '\b\b\b\bjustice', 'hanged man.',
             '\b\b\b\bdeath.', '\b\b\b\btemperance.', 'devil.', 'tower.', 'star.', 'moon.', 'sun.',
             '\b\b\b\bjudgement.', 'world.', 'fool.']

    table = []
    for i in deck:
        tempcard = []
        tempcard.append(i % 4)
        if deck[i] < 56:
            tempcard.append(deck[i] % 14)
        else:
            tempcard.append(deck[i] % 56)
        tempcard.append(deck[i] / 4)
        table.append(tempcard)


def main():
    deck = shuf()
    parseint(deck)


if __name__ == "__main__":
    main()
