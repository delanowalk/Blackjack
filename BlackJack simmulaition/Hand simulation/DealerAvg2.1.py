# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:35:04 2023

@author: walker

Avg dealer count at a true 0
"""

from random import randint
import numpy as np
from numpy import ndarray


def deck_amount(decks):
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


"Defines the deck and the values for each card two slots cause Aces suck"


def sum_cards(arr):
    deck = deck_amount(1)
    sum_arr = 0
    length = len(arr)
    n = 1
    i = 0
    while i < length:
        sum_arr = sum_arr + int(deck[arr[i]][1])

        if arr[0] == 'A' and arr[1] == 'A' and i == 1:
            sum_arr = int(deck[arr[0]][2]) + int(deck[arr[1]][1])

        if i > 1 and deck[arr[i]][1] == 11:
            sum_arr = sum_arr + int(deck[arr[i]][2])
        i += 1
        while sum_arr > 21 and n < length:
            sum_arr = int(deck[arr[0]][2])
            while n < length:
                sum_arr = sum_arr + int(deck[arr[n]][2])
                n += 1
                i = n
    return sum_arr


"sum for array, edge cases and not greater then 21"


def dealer_hand_21(dealer_card1: object) -> object:
    deck = deck_amount(1)
    dealer_info = [dealer_card1]
    index_card = np.array(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

    dealer_card2 = index_card[np.random.randint(13)]

    dealer_info.append(dealer_card2)

    if deck[dealer_card1][1] == 11 and deck[dealer_card2][1] == 11:
        dealer_sum = deck[dealer_card1][1] + deck[dealer_card2][2]

    else:
        dealer_sum = deck[dealer_card1][1] + deck[dealer_card2][1]

    while dealer_sum < 17:
        dealer_hit_card = index_card[np.random.randint(13)]
        dealer_info.append(dealer_hit_card)
        dealer_sum = sum_cards(dealer_info)

        if dealer_sum > 21:
            return dealer_sum

        elif dealer_sum >= 17:
            return dealer_sum

    return dealer_sum


def dealer_avg_game(dealer_card1: object, amount_of_hands):
    count_17 = 0
    count_18 = 0
    count_19 = 0
    count_20 = 0
    count_21 = 0
    count_bust = 0
    hands_played = 0
    while amount_of_hands > hands_played:
        dealer_hand = dealer_hand_21(dealer_card1)

        if dealer_hand > 21:
            count_bust += 1
            hands_played += 1

        elif dealer_hand == 17:
            count_17 += 1
            hands_played += 1

        elif dealer_hand == 18:
            count_18 += 1
            hands_played += 1

        elif dealer_hand == 19:
            count_19 += 1
            hands_played += 1

        elif dealer_hand == 20:
            count_20 += 1
            hands_played += 1

        elif dealer_hand == 21:
            count_21 += 1
            hands_played += 1

    percent_17 = 100*(count_17/amount_of_hands)
    percent_18 = 100*(count_18/amount_of_hands)
    percent_19 = 100*(count_19/amount_of_hands)
    percent_20 = 100*(count_20/amount_of_hands)
    percent_21 = 100*(count_21/amount_of_hands)   
    percent_bust = 100*(count_bust/amount_of_hands)

    dealer_avg = (count_17 * 17 + count_18 * 18 + count_19 * 19 + count_20 * 20 + count_21 * 21) / (amount_of_hands - count_bust)

    print(f'Amount of 17    :{count_17}')
    print(f'Amount of 18    :{count_18}')
    print(f'Amount of 19    :{count_19}')
    print(f'Amount of 20    :{count_20}')
    print(f'Amount of 21    :{count_21}')
    print(f'Amount of bust  :{count_bust}')
    print("")
    print(f'Percent of 17   :{percent_17}')
    print(f'Percent of 18   :{percent_18}')
    print(f'Percent of 19   :{percent_19}')
    print(f'Percent of 20   :{percent_20}')
    print(f'Percent of 21   :{percent_21}')
    print(f'Percent of Bust :{percent_bust}')
    print(f'dealer_avg      :{dealer_avg}')

    print("End of game")
    return


dealer_avg_game('7', 10000)


