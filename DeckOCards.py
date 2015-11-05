__author__ = 'blarson2'

# !/usr/local/bin/python

import random
import datetime

def translate(deck) -> list:
    hand = ['north has the ', 'east has the ', 'south has the ', 'west has the ']
    minor = ['ace ', 'deuce ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ',
             'nine ', 'ten ', 'page ', 'knight ', 'queen ', 'king ']
    suit = ['of wands.', 'of cups.', 'of swords.', 'of coins.', '.']

    major = ['magician.', 'priestess.', 'empress.', 'emperor.', 'hierophant.', 'lovers.', 'chariot.',
             '\b\b\b\bstrength.', 'hermit.', '\b\b\b\bfortune.', '\b\b\b\bjustice', 'hanged man.',
             '\b\b\b\bdeath.', '\b\b\b\btemperance.', 'devil.', 'tower.', 'star.', 'moon.', 'sun.',
             '\b\b\b\bjudgement.', 'world.', 'fool.']

    table = []

    for i in range(78):
        table.append(hand[i % 4])
        if deck[i] < 56:
            table[i] += minor[deck[i % 14]]
            table[i] += suit[deck[i // 14]]
        else:
            table[i] += major[deck[i % 56]]
            table[i] += suit[4]

    for i in table:
        print(table[i])
    return table


def main():
    deck = []
    for i in range(78):
        deck.append(0)
        deck[i] = i
        print(deck[i])

    random.seed(datetime)
    random.shuffle(deck)
    table = translate(deck)


if __name__ == "__main__":
    main()
