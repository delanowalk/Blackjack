# -*- coding: utf-8 -*-
"""
Created on Thur Mar 9 2:09:58 2023

@author: dwalker

#S17 game
this is where a dealer stands on a soft 17
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






"soft hand ablitily to double or surrender"


"""
is soft soft = 0
is hard soft = 1
"""

"should I split"


def soft_hard(arr):
    deck = deck_amount(1)
    k = 0
    soft = 1
    for i in arr:
        if i == 'A':
            sum_c = 10
            while k < len(arr):
                sum_c = sum_c + deck[arr[k]][2]
                k += 1
            if sum_c > 21:
                soft = 1
                return soft
            else:
                soft = 0
                return soft
        if i != 'A':
            soft = 1
            return soft
    return soft


def should_split(player_info, dealer_card, true_count):
    deck = deck_amount(1)
    if player_info[0] == 'A':
        split = 1
        return split

    elif deck[player_info[0]][1] == 10:
        if dealer_card == '4':
            if true_count >= 6:
                split = 1
                return split
            else:
                split = 0
                return split
        elif dealer_card == '5':
            if true_count >= 5:
                split = 1
                return split
            else:
                split = 0
                return split
        elif dealer_card == '6':
            if true_count >= 4:
                split = 1
                return split
            else:
                split = 0
                return split

    elif player_info[0] == '9':
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6' or dealer_card == '8' or dealer_card == '9':
            split = 1
            return split
        else:
            split = 0
            return split

    elif player_info[0] == '8':
        split = 1
        return split

    elif player_info[0] == '7':
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6' or dealer_card == '7':
            split = 1
            return split
        else:
            split = 0
            return split

    elif player_info[0] == '6':
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            split = 1
            return split
        else:
            split = 0
            return split

    elif player_info[0] == '5':
        split = 0
        return split

    elif player_info[0] == '4':
        if dealer_card == '5' or dealer_card == '6':
            split = 1
            return split
        else:
            split = 0
            return split

    elif player_info[0] == '3':
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6' or dealer_card == '7':
            split = 1
            return split
        else:
            split = 0
            return split

    elif player_info[0] == '2':
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6' or dealer_card == '7':
            split = 1
            return split
        else:
            split = 0
            return split

    else:
        split = 0
        return split


def soft_hand_stg_1(player_cards, dealer_card, true_count):
    player_sum = sum_cards(player_cards)
    true_count = round(true_count)

    if player_sum == 21:
        decision = 1

    elif player_sum == 20:
        decision = 1

    elif player_sum == 19:
        if dealer_card == '2' or dealer_card == '3':
            decision = 1
        elif dealer_card == '4':
            if true_count >= 3:
                decision = 3
            else:
                decision = 1
        elif dealer_card == '5':
            if true_count >= 1:
                decision = 3
            else:
                decision = 1
        elif dealer_card == '6':
            if true_count < 0:
                decision = 1
            else:
                decision = 3
        else:
            decision = 1

    elif player_sum == 18:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 3
        elif dealer_card == '7' or dealer_card == '8':
            decision = 1
        elif dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 17:
        if dealer_card == '2':
            if true_count >= 1:
                decision = 3
            else:
                decision = 2
        elif dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 3
        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2
        else:
            decision = 2

    elif player_sum == 16:
        if dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 3
        elif dealer_card == '2' or dealer_card == '3' or dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 15:
        if dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 3
        elif dealer_card == '2' or dealer_card == '3' or dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 14:
        if dealer_card == '5' or dealer_card == '6':
            decision = 3
        elif dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 13:
        if dealer_card == '5' or dealer_card == '6':
            decision = 3
        elif dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2
        else:
            decision = 2

    else:
        decision = 2

    return decision


def hard_hand_stg_1(player_cards, dealer_card, true_count):
    player_sum = sum_cards(player_cards)

    if player_sum == 21:
        decision = 1

    elif player_sum == 20:
        decision = 1

    elif player_sum == 19:
        decision = 1

    elif player_sum == 18:
        decision = 1

    elif player_sum == 17:
        decision = 1

    elif player_sum == 16:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1
        elif dealer_card == '7':
            decision = 2
        elif dealer_card == '8':
            if true_count >= 4:
                decision = 6
            else:
                decision = 2
        elif dealer_card == '9':
            if -1 > true_count < 1:
                decision = 6
            elif true_count > 4:
                decision = 1
            else:
                decision = 2
        elif dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K':
            decision = 6
        elif dealer_card == 'A':
            decision = 6

    elif player_sum == 15:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1

        elif dealer_card == '7' or dealer_card == '8':
            decision = 2

        elif dealer_card == '9':
            if true_count >= 2:
                decision = 6
            else:
                decision = 2

        elif dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K':
            if true_count < 0:
                decision = 2
            else:
                decision = 6

        elif dealer_card == 'A':
            decision = 6

    elif player_sum == 14:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1
        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 13:
        if dealer_card == '2':
            if -1 >= true_count <= 1:
                decision = 2
            else:
                decision = 1
        elif dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1
        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2
        else:
            decision = 1

    elif player_sum == 12:
        if dealer_card == '2':
            if true_count <= 3:
                decision = 1
            else:
                decision = 2

        elif dealer_card == '3':
            if true_count <= 2:
                decision = 1
            else:
                decision = 2

        elif dealer_card == '4':
            if true_count < 0:
                decision = 2
            else:
                decision = 1

        elif dealer_card == '5' or dealer_card == '6':
            decision = 1

        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 11:
        decision = 3

    elif player_sum == 10:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6' or dealer_card == '7' or dealer_card == '8' or dealer_card == '9':
            decision = 3
        elif dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K':
            if true_count >= 4:
                decision = 3
            else:
                decision = 2
        elif dealer_card == 'A':
            if true_count >= 3:
                decision = 3
            else:
                decision = 2

    elif player_sum == 9:
        if dealer_card == '2':
            if true_count >= 1:
                decision = 3
            else:
                decision = 2

        elif dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 3

        elif dealer_card == '7':
            if true_count >= 3:
                decision = 3
            else:
                decision = 2

        elif dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 8:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5':
            decision = 2

        elif dealer_card == '6':
            if true_count >= 2:
                decision = 3
            else:
                decision = 2

        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    else:
        decision = 2

    return decision


def soft_hand_stg_2(player_cards, dealer_card, true_count):
    player_sum = sum_cards(player_cards)
    true_count = round(true_count)

    if player_sum == 20:
        decision = 1

    elif player_sum == 19:
        decision = 1

    elif player_sum == 18:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 2
        elif dealer_card == '7' or dealer_card == '8':
            decision = 1
        elif dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 17:
        decision = 2

    elif player_sum == 16:
        decision = 2

    elif player_sum == 15:
        decision = 2

    elif player_sum == 14:
        decision = 2

    elif player_sum == 13:
        decision = 2

    else:
        decision = 2

    return decision


def hard_hand_stg_2(player_cards, dealer_card, true_count):
    player_sum = sum_cards(player_cards)

    if player_sum == 21:
        decision = 1

    elif player_sum == 20:
        decision = 1

    elif player_sum == 19:
        decision = 1

    elif player_sum == 18:
        decision = 1

    elif player_sum == 17:
        decision = 1

    elif player_sum == 16:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1
        elif dealer_card == '7' or dealer_card == '8':
            decision = 2

        elif dealer_card == '9':
            if true_count >= 4:
                decision = 1
            else:
                decision = 2

        elif dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K':
            if true_count > 0:
                decision = 1
            else:
                decision = 2

        elif dealer_card == 'A':
            if true_count >= 3:
                decision = 1
            else:
                decision = 2

    elif player_sum == 15:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1

        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9':
            decision = 2

        elif dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K':
            if true_count <= 4:
                decision = 1
            else:
                decision = 2

        elif dealer_card == 'A':
            if true_count <= 5:
                decision = 1
            else:
                decision = 2

    elif player_sum == 14:
        if dealer_card == '2' or dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1
        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 13:
        if dealer_card == '2':
            if -1 >= true_count <= 1:
                decision = 2
            else:
                decision = 1

        elif dealer_card == '3' or dealer_card == '4' or dealer_card == '5' or dealer_card == '6':
            decision = 1

        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    elif player_sum == 12:
        if dealer_card == '2':
            if true_count <= 3:
                decision = 1
            else:
                decision = 2

        elif dealer_card == '3':
            if true_count <= 2:
                decision = 1
            else:
                decision = 2

        elif dealer_card == '4':
            if true_count < 0:
                decision = 2
            else:
                decision = 1

        elif dealer_card == '5' or dealer_card == '6':
            decision = 1

        elif dealer_card == '7' or dealer_card == '8' or dealer_card == '9' or dealer_card == '10' or dealer_card == 'J' or dealer_card == 'Q' or dealer_card == 'K' or dealer_card == 'A':
            decision = 2

    else:
        decision = 2

    return decision


def basic_stg(player_cards, dealer_card, count, insurance_d):
    deck = deck_amount(1)
    if dealer_card == 'A' and count >= 3 and insurance_d == 0:
        decision = "5"
        print(f'decision:  {decision}')
        return decision
    if len(player_cards) == 2:
        if player_cards[0] == player_cards[1]:
            if should_split(player_cards, dealer_card, count) == 1:
                print(f'yes split {player_cards}')
                decision = "4"
                print(f'decision:  {decision}')
                return decision
            else:
                print(f'do not split {player_cards}')
                if soft_hard(player_cards) == 0:
                    decision = soft_hand_stg_1(player_cards, dealer_card, count)
                    print(f'decision:  {decision}')
                    return decision
                elif soft_hard(player_cards) == 1:
                    decision = hard_hand_stg_1(player_cards, dealer_card, count)
                    print(f'decision:  {decision}')
                    return decision

        elif soft_hard(player_cards) == 0:
            decision = soft_hand_stg_1(player_cards, dealer_card, count)
            print(f'decision:  {decision}')
            return decision
        elif soft_hard(player_cards) == 1:
            decision = hard_hand_stg_1(player_cards, dealer_card, count)
            print(f'decision:  {decision}')
            return decision
    else:
        if soft_hard(player_cards) == 0:
            decision = soft_hand_stg_2(player_cards, dealer_card, count)
            print(f'decision:  {decision}')
            return decision
        elif soft_hard(player_cards) == 1:
            decision = hard_hand_stg_2(player_cards, dealer_card, count)
            print(f'decision:  {decision}')
            return decision


"basic strategy"


def bet_spread(true_count):
    true_count = round(true_count)
    if true_count <= 0:
        bet = 2
    elif true_count == 1:
        bet = 4
    elif true_count == 2:
        bet = 8
    elif true_count == 3:
        bet = 10
    elif true_count == 4:
        bet = 20
    elif true_count >= 5:
        bet = 30
    return bet


"""
create a bet spread
I used the bet spread I was using at home 
"""


