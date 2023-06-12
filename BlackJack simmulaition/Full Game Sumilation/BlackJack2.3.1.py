"""
Created on Mon April 24 10:30:47 2023

@author: dwalker

#rewroking shit
updated from BlackJack2.2.4
playing with notes on optimal play
playable before I put in error trackering
"""

import random
from random import randint
import numpy as np
from numpy import ndarray

error = 0
choices = 0

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


def shoe(amount_of_decks):
    deck = deck_amount(amount_of_decks)
    index_card = np.array(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    cards_left = 0
    shuffle = np.array([])
    for x in deck.keys():
        cards_left = cards_left + (deck[x][0])
    while cards_left > 0:
        index_c = index_card[np.random.randint(13)]
        if deck[index_c][0] > 0:
            deck[index_c][0] = deck[index_c][0] - 1
            cards_left = cards_left - 1
            shuffle = np.append(shuffle, index_c)
        if cards_left == 0:
            return shuffle


"Creates the shuffle as an array that we will count though"


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

        if i > 1 and deck[arr[i]][1] == 11 and sum_arr > 21:
            sum_arr = sum_arr + int(deck[arr[i]][2]) - int(deck[arr[i]][1])
        i += 1
        while sum_arr > 21 and n < length:
            sum_arr = int(deck[arr[0]][2])
            while n < length:
                sum_arr = sum_arr + int(deck[arr[n]][2])
                n += 1
                i = n
    return sum_arr


"sum for array, edge cases and not greater then 21"


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


"soft or hard hand"


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
            decision = 1
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
        # print(f'decision:  {decision}')
        return decision
    if len(player_cards) == 2:
        if player_cards[0] == player_cards[1]:
            if should_split(player_cards, dealer_card, count) == 1:
                print(f'yes split {player_cards}')
                decision = "4"
                # print(f'decision:  {decision}')
                return decision
            else:
                print(f'do not split {player_cards}')
                if soft_hard(player_cards) == 0:
                    decision = soft_hand_stg_1(player_cards, dealer_card, count)
                    # print(f'decision:  {decision}')
                    return decision
                elif soft_hard(player_cards) == 1:
                    decision = hard_hand_stg_1(player_cards, dealer_card, count)
                    # print(f'decision:  {decision}')
                    return decision

        elif soft_hard(player_cards) == 0:
            decision = soft_hand_stg_1(player_cards, dealer_card, count)
            # print(f'decision:  {decision}')
            return decision
        elif soft_hard(player_cards) == 1:
            decision = hard_hand_stg_1(player_cards, dealer_card, count)
            # print(f'decision:  {decision}')
            return decision
    else:
        if soft_hard(player_cards) == 0:
            decision = soft_hand_stg_2(player_cards, dealer_card, count)
            # print(f'decision:  {decision}')
            return decision
        elif soft_hard(player_cards) == 1:
            decision = hard_hand_stg_2(player_cards, dealer_card, count)
            # print(f'decision:  {decision}')
            return decision


# print(basic_stg(['5', 'A'], 'Q', 3, 0))
"basic strategy"


def counting_card(cards_delt, shuffle):
    decks = 8
    cards_left = ((decks * 52) - cards_delt) / 52
    deck = deck_amount(1)
    high_low_count = 0
    i = 0
    while i < cards_delt:
        if deck[shuffle[i]][1] > 9:
            high_low_count += -1
            i += 1
        elif deck[shuffle[i]][1] < 7:
            high_low_count += 1
            i += 1
        else:
            i += 1
    true_count = high_low_count / cards_left
    return high_low_count, true_count


"counting cards high low count 10 to A -1: 2 to 6 +1"


def bet_spread(true_count):
    if true_count < 1:
        bet = 0
    elif 1 <= true_count < 2:
        bet = 4
    elif 2 <= true_count < 3:
        bet = 8
    elif 3 <= true_count < 4:
        bet = 10
    elif 4 <= true_count < 5:
        bet = 20
    elif true_count >= 5:
        bet = 30
    else:
        bet = 2
    return bet


'bet spread'


def split(shuffle, cards_delt, player_cards):
    deck = deck_amount(1)
    if deck[player_cards[0]][1] == deck[player_cards[1]][1]:
        player_split_1 = np.array([player_cards[0]])
        player_split_1 = np.append(player_split_1, shuffle[cards_delt])

        cards_delt += 1

        player_split_2 = np.array([player_cards[1]])
        player_split_2 = np.append(player_split_2, shuffle[cards_delt])
        cards_delt += 1

        return player_split_1, player_split_2, cards_delt

    elif deck[player_cards[0]][1] != deck[player_cards[1]][1]:
        print('Can not split Cards are different')
        player_split_1 = np.array(['100', '100'])
        player_split_2 = np.array(['100', '100'])
        return player_split_1, player_split_2, cards_delt


'split hands pt 1'


def split_info(player_info, shuffle, cards_delt, i):
    ''' words


     '''
    player_cards = player_info['player_hand ' + str(i + 1)]['player_cards']
    player_split_1, player_split_2, cards_delt = split(shuffle, cards_delt, player_cards)

    if player_split_1[0] == '100':
        fucken_idiot = 100
        return player_info, cards_delt, fucken_idiot

    last_hand = len(player_info)
    bet = player_info['player_hand ' + str(i + 1)]['bet']
    del player_info['player_hand ' + str(i + 1)]

    player_info['player_hand ' + str(i + 1)] = {}
    sum_cards1 = sum_cards(player_split_1)
    player_info['player_hand ' + str(i + 1)]['player_sum'] = sum_cards1
    player_info['player_hand ' + str(i + 1)]['player_cards'] = player_split_1
    player_info['player_hand ' + str(i + 1)]['bet'] = bet

    player_info['player_hand ' + str(last_hand + 1)] = {}
    sum_cards2 = sum_cards(player_split_2)
    player_info['player_hand ' + str(last_hand + 1)]['player_sum'] = sum_cards2
    player_info['player_hand ' + str(last_hand + 1)]['player_cards'] = player_split_2
    player_info['player_hand ' + str(last_hand + 1)]['bet'] = bet
    fucken_idiot = 0

    return player_info, cards_delt, fucken_idiot


'split hands function pt2'


def insurance_21(dealer_info, bet, bankroll):
    bet = int(bet)
    bankroll = int(bankroll)
    dealer_sum = sum_cards(dealer_info)
    insure = 0
    if dealer_info[0] == 'A':
        if dealer_sum == 21:
            bankroll = bankroll + bet
            print("win insurance bet")
            print(f"player bankroll  : {bankroll}")
            return bankroll

        elif dealer_sum != 21:
            bankroll = bankroll - (bet / 2)
            print("lose insurance bet")
            print(f"player bankroll  : {bankroll}")
            return bankroll

    else:
        print("dealer not showing ace stupid")
        return bankroll


"insurance side bet"


def deal_player_hand(shuffle, cards_delt):
    player_info: ndarray = np.array([])

    player_card1 = shuffle[cards_delt]
    cards_delt += 1
    player_card2 = shuffle[cards_delt]
    cards_delt += 1

    player_info = np.append(player_info, player_card1)
    player_info = np.append(player_info, player_card2)

    player_sum = sum_cards(player_info)

    # print(f"player cards     : {player_info[0], player_info[1]}")
    # print(f"player sum       : {player_sum}")
    return player_info, cards_delt


"Dealer player hand"


def deal_dealer_hand(shuffle, cards_delt):
    dealer_info: ndarray = np.array([])

    dealer_card1 = shuffle[cards_delt]
    cards_delt += 1
    dealer_card2 = shuffle[cards_delt]
    cards_delt += 1

    dealer_info = np.append(dealer_info, dealer_card1)
    dealer_info = np.append(dealer_info, dealer_card2)

    return dealer_info, cards_delt


"deal dealer cards"


def dealer_hand_h17(shuffle, cards_delt, dealer_info):
    dealer_sum = sum_cards(dealer_info)
    while dealer_sum <= 17:
        if dealer_sum == 17:
            if soft_hard(dealer_info):
                dealer_hit_card = shuffle[cards_delt]
                cards_delt += 1
                dealer_info = np.append(dealer_info, dealer_hit_card)
                dealer_sum = sum_cards(dealer_info)
            else:
                print(f"dealer cards     : {dealer_info}")
                return dealer_sum

        elif dealer_sum != 17:
            dealer_hit_card = shuffle[cards_delt]
            cards_delt += 1
            dealer_info = np.append(dealer_info, dealer_hit_card)
            dealer_sum = sum_cards(dealer_info)
        else:
            print(f"dealer cards     : {dealer_info}")
            return dealer_sum

    print(f"dealer cards     : {dealer_info}")
    return dealer_sum, dealer_info, cards_delt


"hit 17 dealer hits on a soft 17"


def dealer_hand_s17(shuffle, cards_delt, dealer_info):
    dealer_sum = sum_cards(dealer_info)
    while dealer_sum < 17:
        dealer_hit_card = shuffle[cards_delt]
        cards_delt += 1
        dealer_info = np.append(dealer_info, dealer_hit_card)
        dealer_sum = sum_cards(dealer_info)

    print(f"dealer cards     : {dealer_info}")

    return dealer_sum, dealer_info, cards_delt


"stand 17 dealer stands on a soft 17"


def player_hit(shuffle, cards_delt, player_cards):
    player_hit_card = shuffle[cards_delt]
    cards_delt += 1
    player_cards = np.append(player_cards, player_hit_card)
    player_sum = sum_cards(player_cards)

    return player_cards, player_sum, cards_delt


"hits for the player"


def results(player_info, dealer_sum, player_won, dealer_won, bet, bankroll):
    bankroll = int(bankroll)
    bet = int(bet)

    for i in range(len(player_info)):
        cards = len(player_info['player_hand ' + str(i + 1)]['player_cards'])
        player_sum = player_info['player_hand ' + str(i + 1)]['player_sum']
        bet = player_info['player_hand ' + str(i + 1)]['bet']
        bet = int(bet)
        print('')
        if player_sum > 21:
            dealer_won += 1
            bankroll = bankroll - bet
            print(f"dealer sum       : {dealer_sum}")
            print(f"player sum       : {player_sum}")
            print(f"dealer won")
            print(f"player bankroll  : {bankroll}")

        elif player_sum == 0:
            dealer_won += 1
            bankroll = bankroll - (bet / 2)
            print(f"dealer sum       : {dealer_sum}")
            print(f"player sum       : {player_sum}")
            print(f"dealer won")
            print(f"player bankroll  : {bankroll}")

        elif dealer_sum > 21:
            player_won += 1
            bankroll = bankroll + bet
            if player_sum == 21:
                bankroll = bankroll + (bet / 2)
            print(f"dealer sum       : {dealer_sum}")
            print(f"player sum       : {player_sum}")
            print(f"player won")
            print(f"player bankroll  : {bankroll}")

        elif dealer_sum > player_sum:
            dealer_won += 1
            bankroll = bankroll - bet
            print(f"dealer sum       : {dealer_sum}")
            print(f"player sum       : {player_sum}")
            print(f"dealer won")
            print(f"player bankroll  : {bankroll}")

        elif player_sum > dealer_sum:
            player_won += 1
            bankroll = bankroll + bet
            if player_sum == 21:
                if cards == 2:
                    bankroll = bankroll + (bet / 2)
                else:
                    bankroll = bankroll
            print(f"dealer sum          :{dealer_sum}")
            print(f"player sum          :{player_sum}")
            print(f"player won")
            print(f"player bankroll     :{bankroll}")

        elif player_sum == dealer_sum:
            bankroll = bankroll
            print(f"dealer sum          :{dealer_sum}")
            print(f"player sum          :{player_sum}")
            print(f"push")
            print(f"player bankroll     :{bankroll}")

    return player_won, dealer_won, bankroll


"results"


def player_hand_21_2(shuffle, cards_delt, player_info, dealer_info, i):
    player_cards = player_info['player_hand ' + str(i + 1)]['player_cards']
    player_sum = sum_cards(player_cards)
    print(f'player cards     :{player_cards}')
    print(f'player sum       :{player_sum}')
    decision = "100"
    insurance_d = 1
    while player_sum < 21:
        dealer_card = dealer_info[0]
        high_low_count, count = counting_card(cards_delt, shuffle)
        s_decision = basic_stg(player_cards, dealer_card, count, insurance_d)
        s_decision = str(s_decision)

        decision = input("stand(1), hit(2), double(3), split(4), insurance(5) or surrender(6)      \n:")

        if s_decision != decision:
            print(f"should:{s_decision}")

        if decision == "1":
            print('')
            return player_info, cards_delt, decision
        elif decision == "2":
            player_cards, player_sum, cards_delt = player_hit(shuffle, cards_delt, player_cards)
            print(f'player cards     :{player_cards}')
            print(f'player sum       :{player_sum}')
            player_info['player_hand ' + str(i + 1)]['player_cards'] = player_cards
            player_info['player_hand ' + str(i + 1)]['player_sum'] = player_sum
        else:
            print("put a number dib-shit")
    return player_info, cards_delt, decision


"choice after hitting"


def player_hand_21_1(player_info, dealer_info, shuffle, cards_delt, i, bankroll, insurance_d):
    player_cards = player_info['player_hand ' + str(i + 1)]['player_cards']
    player_sum = sum_cards(player_cards)
    bet = player_info['player_hand ' + str(i + 1)]['bet']
    print(f'player cards     :{player_cards}')
    print(f'player sum       :{player_sum}')
    dealer_card = dealer_info[0]
    high_low_count, count = counting_card(cards_delt, shuffle)
    s_decision = basic_stg(player_cards, dealer_card, count, insurance_d)
    s_decision = str(s_decision)
    bankroll = int(bankroll)
    print("")
    decision = input("stand(1), hit(2), double(3), split(4), insurance(5) or surrender(6)      \n:")

    if s_decision != decision:
        print(f"should:{s_decision}")

    # stand
    if decision == "1":
        return player_info, cards_delt, bankroll, decision, i

    # hit
    if decision == "2":
        player_cards, player_sum, cards_delt = player_hit(shuffle, cards_delt, player_cards)
        player_info['player_hand ' + str(i + 1)] = {'player_sum': player_sum, 'player_cards': player_cards, 'bet': bet}
        player_info, cards_delt, decision = player_hand_21_2(shuffle, cards_delt, player_info, dealer_info, i)
        return player_info, cards_delt, bankroll, decision, i

    # double
    elif decision == "3":
        player_cards, player_sum, cards_delt = player_hit(shuffle, cards_delt, player_cards)
        bet = player_info['player_hand ' + str(i + 1)]['bet']
        player_info['player_hand ' + str(i + 1)] = {'player_sum': player_sum, 'player_cards': player_cards,
                                                    'bet': int(bet) * 2}
        print(f'player cards     :{player_cards}')
        print(f'player sum       :{player_sum}')
        return player_info, cards_delt, bankroll, decision, i

    # split
    elif decision == "4":
        player_info, cards_delt, fucken_idiot = split_info(player_info, shuffle, cards_delt, i)
        if fucken_idiot == 100:
            print('Fuck you, you canot split when the cards are different you are the problem')
            player_info, cards_delt, bankroll, decision, i = player_hand_21_1(player_info, dealer_info, shuffle,
                                                                              cards_delt, i, bankroll, insurance_d)
            return player_info, cards_delt, bankroll, decision, i
        elif fucken_idiot == 0:
            player_info, cards_delt, bankroll, decision, i = player_hand_21_1(player_info, dealer_info,
                                                                              shuffle, cards_delt, i, bankroll,
                                                                              insurance_d)
            player_info, cards_delt, bankroll, decision, j = player_hand_21_1(player_info, dealer_info,
                                                                              shuffle, cards_delt, len(player_info) - 1,
                                                                              bankroll, insurance_d)
            return player_info, cards_delt, bankroll, decision, i

    # insurance
    elif decision == "5":
        hands = len(player_info)
        bankroll = insurance_21(dealer_info, bet, bankroll)
        insurance_d = 1
        player_info, cards_delt, bankroll, decision, i = player_hand_21_1(player_info, dealer_info,
                                                                          shuffle, cards_delt, i, bankroll, insurance_d)
        return player_info, cards_delt, bankroll, decision, i

    # late surrender
    elif decision == "6":
        print("Fucken pussy")
        player_info['player_hand ' + str(i + 1)]['player_sum'] = 0
        player_info['player_hand ' + str(i + 1)]['bet'] = bet / 2
        return player_info, cards_delt, bankroll, decision, i

    else:
        print("put a number dib-shit")
    return player_info, cards_delt, bankroll, decision, i


"first time choice after the cards are delt"


def play_game(player_info, dealer_info, shuffle, cards_delt, bankroll):
    i = 0
    hands = len(player_info)
    insurance_d = 0
    while i < hands:
        player_info, cards_delt, bankroll, decision, i = player_hand_21_1(player_info, dealer_info,
                                                                          shuffle, cards_delt, i, bankroll, insurance_d)
        print('')
        i += 1
    return player_info, cards_delt, bankroll


'plays though hands'


def game_21(amount_of_decks, bankroll):
    bankroll = int(bankroll)
    shuffle = shoe(amount_of_decks)
    deck = deck_amount(amount_of_decks)
    cards_delt = 0
    dealer_won = 0
    player_won = 0
    while cards_delt < (len(shuffle) - randint(30, 52)):
        decks_left = (len(shuffle) - cards_delt) / 52
        high_low_count, true_count = counting_card(cards_delt, shuffle)
        true_count = high_low_count / decks_left

        print("")
        print(f'Cards Delt       :{cards_delt}')
        print(f'Decks Left       :{decks_left}')
        print(f'Running Count    :{high_low_count}')
        print(f'True Count       :{true_count}')
        print(f'Dealer Won       :{dealer_won}')
        print(f'Player Won       :{player_won}')
        print(f"player bankroll  :{bankroll}")
        print("")
        print("New Hand")

        if bankroll <= 0:
            print(f"you fucked we coming for that social security check too")

        """hands = input("How Many Hands   :")"""
        hands = 1
        hands = int(hands)

        player_info = {}
        dealer_info, cards_delt = deal_dealer_hand(shuffle, cards_delt)

        for i in range(hands):
            player_cards, cards_delt = deal_player_hand(shuffle, cards_delt)
            player_sum = sum_cards(player_cards)
            s_bet = bet_spread(true_count)
            print("")
            bet = input("bet              :")
            print(f'bet: {bet}')
            bet = int(bet)
            if s_bet != bet:
                print(f'bet should be: {s_bet}')
            player_info['player_hand ' + str(i + 1)] = {'player_sum': player_sum, 'player_cards': player_cards,
                                                        'bet': bet}
            i += 1

        "betting for loop"

        print('')
        print(f"dealer card 1    : {dealer_info[0]}")
        player_info, cards_delt, bankroll = play_game(player_info, dealer_info, shuffle, cards_delt, bankroll)

        print('')
        dealer_sum, dealer_info, cards_delt = dealer_hand_s17(shuffle, cards_delt, dealer_info)
        player_won, dealer_won, bankroll = results(player_info, dealer_sum, player_won, dealer_won, bet, bankroll)

    print("")
    print("End of Shoe")
    return bankroll


"""
def gambling_additic(bankroll):
    shoes = 0
    win = 0
    lose = 0
    t = 0

    while bankroll > 0:
        while t < 10:
            bankroll = game_21(8, bankroll)
            shoes += 1
            if bankroll > 2000:
                print("fuck Yeah")
                print(f'amount of shoes {shoes}')
                bankroll = 1000
                t += 1
                win += 1
            elif bankroll < 0:
                bankroll = 1000
                t += 1
                lose += 1
        bankroll = 0
        print(f'win {win}')
        print(f'lose  {lose}')
        t += 1
"""

game_21(4, 1000)
