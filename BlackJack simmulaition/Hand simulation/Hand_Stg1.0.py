# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:35:04 2023

@author: walker

Avg dealer count at a true 0
stand 17 game

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


def counting_card(cards_delt, shuffle):
    cards_delt = cards_delt
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
    return high_low_count


"counting cards high low count 10 to A -1: 2 to 6 +1"


def shoe(amount_of_decks, true_count):

    true_count = true_count
    deck = deck_amount(1)
    cards_changed = true_count
    neg_cards = np.array(['2', '3', '4', '5', '6'])
    pos_cards = np.array(['10', 'J', 'Q', 'K', 'A'])

    if true_count > 0:
        while cards_changed > 0:
            neg_chosen_card = neg_cards[np.random.randint(5)]
            deck[neg_chosen_card][0] = deck[neg_chosen_card][0] - 1
            cards_changed -= 1

            pos_chosen_card = pos_cards[np.random.randint(5)]
            deck[pos_chosen_card][0] = deck[pos_chosen_card][0] + 1
            cards_changed -= 1

    if true_count < 0:
        while cards_changed < 0:
            neg_chosen_card = neg_cards[np.random.randint(5)]
            deck[neg_chosen_card][0] = deck[neg_chosen_card][0] - 1
            cards_changed += 1

            pos_chosen_card = pos_cards[np.random.randint(5)]
            deck[pos_chosen_card][0] = deck[pos_chosen_card][0] + 1
            cards_changed += 1

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
            print(counting_card(len(shuffle), shuffle))
            print(shuffle)
            return shuffle


"""
Creates the shuffle as an array that we will count though 
we are going to manipulate this function to 
give us a positive or negative true count though
"""


def dealer_hand_21(dealer_card1, true_count, shuffle):
    deck = deck_amount(1)
    amount_of_decks = 4
    dealer_info = [dealer_card1]

    dealer_card2 = shuffle[np.random.randint(len(shuffle))]

    dealer_info.append(dealer_card2)

    if deck[dealer_card1][1] == 11 and deck[dealer_card2][1] == 11:
        dealer_sum = deck[dealer_card1][1] + deck[dealer_card2][2]

    else:
        dealer_sum = deck[dealer_card1][1] + deck[dealer_card2][1]

    while dealer_sum < 17:
        dealer_hit_card = shuffle[np.random.randint(len(shuffle))]
        dealer_info.append(dealer_hit_card)
        dealer_sum = sum_cards(dealer_info)

        if dealer_sum > 21:
            return dealer_sum

        elif dealer_sum >= 17:
            return dealer_sum

    return dealer_sum


def player_hand_21(player_card1, player_card2, shuffle):
    deck = deck_amount(1)
    player_info = [player_card1, player_card2]

    player_hit_card = shuffle[np.random.randint(len(shuffle))]
    player_info.append(player_hit_card)
    player_sum = sum_cards(player_info)

    return player_sum


def dealer_avg_game(dealer_card1, amount_of_hands, true_count):
    count_17 = 0
    count_18 = 0
    count_19 = 0
    count_20 = 0
    count_21 = 0
    count_bust = 0
    hands_played = 0
    shuffle = shoe(10, true_count)
    while amount_of_hands > hands_played:
        dealer_hand = dealer_hand_21(dealer_card1, true_count, shuffle)

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
    return percent_17, percent_18, percent_19, percent_20, percent_21, percent_bust


def player_avg_game(player_card1: object, player_card2, amount_of_hands, true_count):
    count_17 = 0
    count_18 = 0
    count_19 = 0
    count_20 = 0
    count_21 = 0
    count_bust = 0
    count_under_17 = 0
    hands_played = 0
    player_total = 0
    shuffle = shoe(10, true_count)
    while amount_of_hands > hands_played:
        player_hand = player_hand_21(player_card1, player_card2, shuffle)

        if player_hand > 21:
            count_bust += 1
            hands_played += 1

        elif player_hand == 17:
            count_17 += 1
            hands_played += 1

        elif player_hand == 18:
            count_18 += 1
            hands_played += 1

        elif player_hand == 19:
            count_19 += 1
            hands_played += 1

        elif player_hand == 20:
            count_20 += 1
            hands_played += 1

        elif player_hand == 21:
            count_21 += 1
            hands_played += 1
        else:
            player_total = player_hand + player_total
            count_under_17 += 1
            hands_played += 1

    percent_17 = 100 * (count_17 / amount_of_hands)
    percent_18 = 100 * (count_18 / amount_of_hands)
    percent_19 = 100 * (count_19 / amount_of_hands)
    percent_20 = 100 * (count_20 / amount_of_hands)
    percent_21 = 100 * (count_21 / amount_of_hands)
    percent_under_17 = 100 * (count_under_17 / amount_of_hands)
    percent_bust = 100 * (count_bust / amount_of_hands)

    avg_player_total = (player_total + count_17*17 + count_18*18 + count_19*19 + count_20*20 + count_21*21)/(amount_of_hands - count_bust)

    print(f'Amount Under 17  :{count_under_17}')
    print(f'Amount of 17     :{count_17}')
    print(f'Amount of 18     :{count_18}')
    print(f'Amount of 19     :{count_19}')
    print(f'Amount of 20     :{count_20}')
    print(f'Amount of 21     :{count_21}')
    print(f'Amount of bust   :{count_bust}')
    print("")
    print(f'Percent Under 17 :{percent_under_17}')
    print(f'Percent of 17    :{percent_17}')
    print(f'Percent of 18    :{percent_18}')
    print(f'Percent of 19    :{percent_19}')
    print(f'Percent of 20    :{percent_20}')
    print(f'Percent of 21    :{percent_21}')
    print(f'Percent of Bust  :{percent_bust}')
    print("")
    print(f'Player Average   :{avg_player_total}')
    print("")
    print("End of game")
    return percent_under_17, percent_17, percent_18, percent_19, percent_20, percent_21, percent_bust


def win_per(dealer_card1, player_card1, player_card2, amount_of_hands, true_count):
    player_sum = sum_cards([player_card1, player_card2])
    player_percent_under_17, player_percent_17, player_percent_18, player_percent_19, player_percent_20, player_percent_21, player_percent_bust = player_avg_game(player_card1, player_card2, amount_of_hands, true_count)
    dealer_percent_17, dealer_percent_18, dealer_percent_19, dealer_percent_20, dealer_percent_21, dealer_percent_bust = dealer_avg_game(dealer_card1, amount_of_hands, true_count)

    hit_tie_percent  = player_percent_17*dealer_percent_17 + player_percent_18*dealer_percent_18 + player_percent_19*dealer_percent_19 + player_percent_20*dealer_percent_20 + player_percent_21*dealer_percent_21

    hit_win_percent  = player_percent_under_17*dealer_percent_bust + player_percent_17*dealer_percent_bust + player_percent_18*(dealer_percent_17 + dealer_percent_bust) + player_percent_19*(dealer_percent_18 + dealer_percent_17 + dealer_percent_bust) + player_percent_20*(dealer_percent_19 + dealer_percent_18 + dealer_percent_17 + dealer_percent_bust) + player_percent_21*(dealer_percent_20 + dealer_percent_19 + dealer_percent_18 + dealer_percent_17 + dealer_percent_bust)

    hit_lose_percent = player_percent_under_17*(dealer_percent_17 + dealer_percent_18 + dealer_percent_19 + dealer_percent_20 + dealer_percent_21) + player_percent_17*(dealer_percent_18 + dealer_percent_19 + dealer_percent_20 + dealer_percent_21) + player_percent_18*(dealer_percent_19 + dealer_percent_20 + dealer_percent_21) + player_percent_19*(dealer_percent_20 + dealer_percent_21) + player_percent_20*dealer_percent_21 + player_percent_bust*100

    if player_sum < 17:
        stand_ties_percent = 0
        stand_wins_percent = dealer_percent_bust
        stand_lose_percent = dealer_percent_17 + dealer_percent_18 + dealer_percent_19 + dealer_percent_20 + dealer_percent_21
    elif player_sum == 17:
        stand_ties_percent = dealer_percent_17
        stand_wins_percent = dealer_percent_bust
        stand_lose_percent = dealer_percent_18 + dealer_percent_19 + dealer_percent_20 + dealer_percent_21
    elif player_sum == 18:
        stand_ties_percent = dealer_percent_18
        stand_wins_percent = dealer_percent_17 + dealer_percent_bust
        stand_lose_percent = dealer_percent_19 + dealer_percent_20 + dealer_percent_21
    elif player_sum == 19:
        stand_ties_percent = dealer_percent_19
        stand_wins_percent = dealer_percent_18 + dealer_percent_17 + dealer_percent_bust
        stand_lose_percent = dealer_percent_20 + dealer_percent_21
    elif player_sum == 20:
        stand_ties_percent = dealer_percent_20
        stand_wins_percent = dealer_percent_19 + dealer_percent_18 + dealer_percent_17 + dealer_percent_bust
        stand_lose_percent = dealer_percent_21
    elif player_sum == 21:
        stand_ties_percent = dealer_percent_21
        stand_wins_percent = dealer_percent_20 + dealer_percent_19 + dealer_percent_18 + dealer_percent_17 + dealer_percent_bust
        stand_lose_percent = 0

    hit_tie_percent = hit_tie_percent / 100
    hit_win_percent = hit_win_percent / 100
    hit_lose_percent = hit_lose_percent / 100

    exp_value_hit = hit_win_percent * 1 - (hit_lose_percent * 1)
    exp_value_double = hit_win_percent * 2 - (hit_lose_percent * 2)
    exp_value_stand = stand_wins_percent * 1 - (stand_lose_percent * 1)

    print("")
    print("if hit/double")
    print(f'tie percent   :{hit_tie_percent}')
    print(f'win percent   :{hit_win_percent}')
    print(f'lose percent  :{hit_lose_percent}')

    print("")
    print("if stand")
    print(f'tie percent   :{stand_ties_percent}')
    print(f'win percent   :{stand_wins_percent}')
    print(f'lose percent  :{stand_lose_percent}')

    print("")
    print(f'exp_value_hit      :{exp_value_hit}')
    print(f'exp_value_double   :{exp_value_double}')
    print(f'exp_value_stand    :{exp_value_stand}')

    print()
    return


win_per('6', 'A', '8', 1000, +4)

