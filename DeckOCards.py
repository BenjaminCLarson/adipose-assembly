__author__ = 'blarson2'

from random import *
import datetime


def shuff(deck):
    temp = deck
    seed(datetime)
    for i in deck:
        popped_elem = temp.index(choice(temp))
        deck.insert(i, temp.pop(popped_elem))

    return temp


def print_deck(table):

    hand_string = ["north has ", "east has ", "south has ", "west has "]
    minor = ["the deuce ", "the three ", "the four ", "the five ", "the six ", "the seven ", "the eight ",
             "the nine ", "the ten ", "the page ", "the knight ", "the queen ", "the king ", "the ace "]

    suit = ["of wands.", "of cups.", "of swords.", "of coins."]

    major = ["the magician.", "the priestess.", "the empress.", "the emperor.", "the hierophant.", "the lovers.",
             "the chariot.", "strength.", "the hermit.", "fortune.", "lust.", "justice","the hanged man.",
             "death.", "temperance.", "the devil.", "the tower.", "the star.", "the moon.", "the sun.",
             "judgement.", "the world.", "the universe.", "the fool."]

    card_string = []

    for i in range(4):
        for j in range(20):
            card = table[i][j]
            cs_ind = ((i * 20) + j)

            if card < 56:
                minor_ind = card%14
                suit_ind = card//20
                card_string.append((hand_string[i] + minor[minor_ind] + suit[suit_ind]))
            else:
                major_ind = card%56
                card_string.append((hand_string[i] + major[major_ind]))

            print (card_string[cs_ind])


def main():

    deck = []

    for i in range(80):
        deck.append(i)

    deck = shuff(deck)
    table = []
    for i in range(4):
        table.append(list())

    for i in range(80):
        table[i%4].append(deck.pop())

    print_deck(table)

if __name__ == "__main__":
    main()
