# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:09:58 2023

@author: dwalker

#shit it works
"""

import numpy as np
from random import randint


def Deck_C(decks):
    count_A = 4 * decks
    count_2 = 4 * decks
    count_3 = 4 * decks
    count_4 = 4 * decks
    count_5 = 4 * decks
    count_6 = 4 * decks
    count_7 = 4 * decks
    count_8 = 4 * decks
    count_9 = 4 * decks
    count_10 = 4 * decks
    count_J = 4 * decks
    count_Q = 4 * decks
    count_K = 4 * decks

    deck = {
        'A': [count_A, 11, 1],
        '2': [count_2, 2, 2],
        '3': [count_3, 3, 3],
        '4': [count_4, 4, 4],
        '5': [count_5, 5, 5],
        '6': [count_6, 6, 6],
        '7': [count_7, 7, 7],
        '8': [count_8, 8, 8],
        '9': [count_9, 9, 9],
        '10': [count_10, 10, 10],
        'J': [count_J, 10, 10],
        'Q': [count_Q, 10, 10],
        'K': [count_K, 10, 10]
    }

    return deck


def Shoe(Amount_of_Decks):
    Deck = Deck_C(Amount_of_Decks)
    Index_Card = np.array(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    Cards_Left = 0
    shuffle = np.array([])
    for x in Deck.keys():
        Cards_Left = Cards_Left + (Deck[x][0])
    while Cards_Left > 0:
        index_c = Index_Card[np.random.randint(13)]
        if Deck[index_c][0] > 0:
            Deck[index_c][0] = Deck[index_c][0] - 1
            Cards_Left = Cards_Left - 1
            shuffle = np.append(shuffle, index_c)
        if Cards_Left == 0:
            print("Cards suffled")
    return shuffle


def Hand_21(shuffle, Deck, cards_delt):
    dealer_sum = 0
    dealer_card1 = shuffle[cards_delt]
    cards_delt += 1
    dealer_card2 = shuffle[cards_delt]
    cards_delt += 1
    dealer_sum = Deck[dealer_card1][1] + Deck[dealer_card2][1]

    player_sum = 0
    player_card1 = shuffle[cards_delt]
    cards_delt += 1
    player_card2 = shuffle[cards_delt]
    cards_delt += 1

    player_sum = Deck[player_card1][1] + Deck[player_card2][1]

    if Deck[player_card1][1] == 11 and Deck[player_card2][1] == 11:
        player_sum = Deck[player_card1][1] + Deck[player_card2][2]

    print(f'dealer card 1    : {dealer_card1}')
    print(f'player cards     : {player_card1, player_card2}')
    print(f'player sum       : {player_sum}')

    while player_sum <= 21:
        hit = input("hit yes or no?")
        if hit == 'yes':
            player_card3 = shuffle[cards_delt]
            cards_delt += 1

            player_sum = player_sum + Deck[player_card3][1]

            if Deck[player_card3][1] == 11 and player_sum > 21:
                player_sum = Deck[player_card1][2] + Deck[player_card2][2] + Deck[player_card2][2]

            print(f'player Hit Card   : {player_card3}')
            print(f'player sum        : {player_sum}')

            while player_sum > 21:
                if player_card3 == 'A':
                    player_sum = Deck[player_card1][2] + Deck[player_card2][2] + Deck[player_card3][2]
                    print(f'player sum        : {player_sum}')


                elif player_card2 == 'A':
                    player_sum = Deck[player_card1][2] + Deck[player_card2][2] + Deck[player_card3][2]
                    print(f'player sum        : {player_sum}')


                elif player_card1 == 'A':
                    player_sum = Deck[player_card1][2] + Deck[player_card2][2] + Deck[player_card3][2]
                    print(f'player sum        : {player_sum}')


                else:
                    print('player busted')
                    print("Dealer won")
                    print(f'dealer card 1     : {dealer_card1}')
                    print(f'dealer card 2     : {dealer_card2}')
                    return cards_delt, player_sum, dealer_sum

        if hit == 'no':
            print(f'dealer cards      : {dealer_card1, dealer_card2}')
            print(f'dealer sum        : {dealer_sum}')
            while dealer_sum < 17:
                dealer_card3 = shuffle[cards_delt]
                dealer_sum = dealer_sum + Deck[dealer_card3][1]
                cards_delt += 1

                if Deck[dealer_card3][1] == 11 and dealer_sum > 21:
                    dealer_sum = dealer_sum - 10

                print(f'dealer hit card   : {dealer_card3}')
                print(f'dealer sum        : {dealer_sum}')

                while dealer_sum > 21:
                    if dealer_card3 == 11:
                        dealer_sum = Deck[dealer_card1][2] + Deck[dealer_card2][2] + Deck[dealer_card3][2]
                        print(f'dealer sum        : {dealer_sum}')


                    elif dealer_card2 == 11:
                        dealer_sum = Deck[dealer_card1][2] + Deck[dealer_card2][2] + Deck[dealer_card3][2]
                        print(f'dealer sum        : {dealer_sum}')


                    elif dealer_card1 == 11:
                        dealer_sum = Deck[dealer_card1][2] + Deck[dealer_card2][2] + Deck[dealer_card3][2]
                        print(f'dealer sum        : {dealer_sum}')


                    else:
                        print('dealer bust')
                        print('player won')
                        return cards_delt, player_sum, dealer_sum

            if dealer_sum > player_sum:
                print(f'player sum        : {player_sum}')
                print(f'dealer sum        : {dealer_sum}')
                print('dealer won')
                return cards_delt, player_sum, dealer_sum

            elif player_sum > dealer_sum:
                print(f'dealer cards      : {dealer_card1, dealer_card2}')
                print(f'dealer sum        : {dealer_sum}')
                print(f'player sum        : {player_sum}')
                print('player won')
                return cards_delt, player_sum, dealer_sum

            elif player_sum == dealer_sum:
                print(f'dealer cards      : {dealer_card1, dealer_card2}')
                print(f'dealer sum        : {dealer_sum}')
                print(f'player sum        : {player_sum}')
                print('push')
                return cards_delt, player_sum, dealer_sum


            else:
                print('shit Idk')
                return

# 2nd
def Game_21(Amount_of_Decks):
    shuffle = Shoe(Amount_of_Decks)
    Deck = Deck_C(Amount_of_Decks)
    cards_delt = 0
    while cards_delt < (len(shuffle) - randint(10, 20)):
        decks_left = (len(shuffle) - cards_delt) / (52)
        print("")
        print(f'Cards Delt {cards_delt}')
        print(f'Decks Left {decks_left}')
        print("New Hand")
        cards_delt = Hand_21(shuffle, Deck, cards_delt)[0]

    print("End of Shoe")
    return


Game_21(1)