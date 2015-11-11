__author__ = 'blarson2'

# !/usr/local/bin/python

from random import *
import datetime

def shuff(deck):
    temp = []
    for i in deck:
        popped_elem = deck.index(choice(deck))
        temp.append(deck.pop(popped_elem))

    return temp

def main():
    minor = ['ace ', 'deuce ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ',
             'nine ', 'ten ', 'page ', 'knight ', 'queen ', 'king ']

    suit = ['of wands.', 'of cups.', 'of swords.', 'of coins.']

    major = ['magician.', 'priestess.', 'empress.', 'emperor.', 'hierophant.', 'lovers.', 'chariot.',
             '\b\b\b\bstrength.', 'hermit.', '\b\b\b\bfortune.', '\b\b\b\blust.', '\b\b\b\bjustice', 'hanged man.',
             '\b\b\b\bdeath.', '\b\b\b\btemperance.', 'devil.', 'tower.', 'star.', 'moon.', 'sun.',
             '\b\b\b\bjudgement.', 'world.', 'universe.', 'fool.']

    deck = []

    for i in range(80):
        deck.append(i)

    table = ['0', '1', '2', '3'],[]

    deck = shuff(deck)

    for i in range(4):
        for j in range(20):
            table[i].append(deck.pop())


if __name__ == "__main__":
    main()
