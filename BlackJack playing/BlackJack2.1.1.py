"""
Created on Mon April 16 4:43:38 2023

@author: dwalker

#rewroking shit
function break down try to make splitting cards work
rework
using dictinatries to hold player Info
not working fully
"""

import random
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
    sum_c = 0
    k = 0
    for i in arr:
        if i == 'A':
            sum_c = 10
            while k < len(arr):
                sum_c = sum_c + deck[arr[k]][2]
                k += 1
            if sum_c > 21:
                soft = False
                return soft
            else:
                soft = True
                return soft
        if i != 'A':
            soft = False
    return soft


"soft or hard hand"


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

    print(f"player cards     : {player_info[0], player_info[1]}")
    print(f"player sum       : {player_sum}")

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

    print(f"dealer card 1    : {dealer_info[0]}")

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
        player_sum = player_info['player_hand ' + str(i+1)]['player_sum']
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
                bankroll = bankroll + (bet/2)
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
                bankroll = bankroll + (bet/2)
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


def player_hand_21_2(shuffle, cards_delt, player_cards, bet):
    player_sum = sum_cards(player_cards)
    print(f'player cards     :{player_cards}')
    print(f'player sum       :{player_sum}')
    bet = int(bet)
    decision = "100"
    while player_sum < 21:
        decision = input("stand(1), hit(2) \n:")
        if decision == "1":
            player_sum = sum_cards(player_cards)
            return player_cards, player_sum, cards_delt, bet, decision

        elif decision == "2":
            player_cards, player_sum, cards_delt = player_hit(shuffle, cards_delt, player_cards)
            print(f'player cards     :{player_cards}')
            print(f'player sum       :{player_sum}')
        else:
            print("put a number dib-shit")

    return player_cards, player_sum, cards_delt, bet, decision


"choice after hitting"


def player_hand_21_1(shuffle, cards_delt, player_info, i, player_cards, dealer_info, bet, bankroll):
    player_sum = sum_cards(player_cards)
    print(f'player cards     :{player_cards}')
    print(f'player sum       :{player_sum}')
    bet = int(bet)
    bankroll = int(bankroll)
    decision = input("stand(1), hit(2), double(3), split(4), insurance(5) or surrender(6)      \n:")

    # stand
    if decision == "1":
        player_sum = sum_cards(player_cards)
        return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision

    # hit
    if decision == "2":
        player_cards, player_sum, cards_delt = player_hit(shuffle, cards_delt, player_cards)
        player_cards, player_sum, cards_delt, bet, decision = player_hand_21_2(shuffle, cards_delt, player_cards, bet)
        return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision

    # double
    elif decision == "3":
        bet = bet * 2
        player_cards, player_sum, cards_delt = player_hit(shuffle, cards_delt, player_cards)
        return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision

    # split
    elif decision == "4":
        player_info = split_info(shuffle, cards_delt, player_info, i, player_cards, bet)
        print("might work")
        return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision

    # insurance
    elif decision == "5":
        bankroll = insurance_21(dealer_info, bet, bankroll)
        return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision

    # late surrender
    elif decision == "6":
        print("Fucken pussy")
        player_sum = 0
        return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision

    else:
        print("put a number dib-shit")
    return player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision


"first time choice after the cards are delt"


def split(shuffle, cards_delt, player_cards):
    deck = deck_amount(1)
    if deck[player_cards[0]][1] == deck[player_cards[1]][1]:
        player_split_1 = np.array([player_cards[0]])
        player_split_1 = np.append(player_split_1, shuffle[cards_delt])

        cards_delt += 1

        player_split_2 = np.array([player_cards[1]])
        player_split_2 = np.append(player_split_2, shuffle[cards_delt])
        cards_delt += 1

        return player_split_1, player_split_2

    elif deck[player_cards[0]][1] != deck[player_cards[1]][1]:
        print('Can not split Cards are different')


def split_info(shuffle, cards_delt, player_info, i, player_cards, bet):
    player_split_1, player_split_2 = split(shuffle, cards_delt, player_cards)
    last_hand = len(player_info)
    del player_info['player_hand ' + str(i+1)]

    player_info['player_hand ' + str(i+1)] = {}
    sum_cards1 = sum_cards(player_split_1)
    player_info['player_hand ' + str(i + 1)]['player_sum'] = sum_cards1
    player_info['player_hand ' + str(i+1)]['player_cards'] = player_split_1
    player_info['player_hand ' + str(i+1)]['bet'] = bet

    player_info['player_hand ' + str(last_hand + 1)] = {}
    sum_cards2 = sum_cards(player_split_2)
    player_info['player_hand ' + str(last_hand + 1)]['player_sum'] = sum_cards2
    player_info['player_hand ' + str(last_hand + 1)]['player_cards'] = player_split_2
    player_info['player_hand ' + str(last_hand + 1)]['bet'] = bet

    return player_info


def game_21(amount_of_decks, bankroll):
    bankroll = int(bankroll)
    shuffle = shoe(amount_of_decks)
    deck = deck_amount(amount_of_decks)
    cards_delt = 0
    dealer_won = 0
    player_won = 0
    while cards_delt < (len(shuffle) - randint(10, 20)):
        decks_left = (len(shuffle) - cards_delt) / 52
        high_low_count = counting_card(cards_delt, shuffle)
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

        #hands = input("How Many Hands   :")
        hands = 2
        hands = int(hands)

        player_info = {}
        dealer_info, cards_delt = deal_dealer_hand(shuffle, cards_delt)

        for i in range(hands):
            print("")
            #bet = input("bet              :")
            bet = 2
            player_cards, cards_delt = deal_player_hand(shuffle, cards_delt)
            player_sum = sum_cards(player_cards)
            player_info['player_hand ' + str(i+1)] = {'player_sum': player_sum, 'player_cards': player_cards, 'bet': bet}
            i += 1

        "betting for loop"

        print('')

        for j in range(hands):
            player_cards = player_info['player_hand ' + str(j+1)]['player_cards']
            player_sum = player_info['player_hand ' + str(j+1)]['player_sum']

            print('')

            player_sum, player_cards, player_info, cards_delt, bet, bankroll, decision = player_hand_21_1(shuffle, cards_delt, player_info, j, player_cards, dealer_info, bet, bankroll)

            player_info['player_hand ' + str(j + 1)]['player_cards'] = player_cards
            player_info['player_hand ' + str(j + 1)]['player_sum'] = player_sum

            if decision == '4':
                player_cards = player_info['player_hand ' + str(j + 1)]['player_cards']
                player_cards, player_sum, cards_delt, bet, decision = player_hand_21_2(shuffle, cards_delt, player_cards, bet)
                player_info['player_hand ' + str(j + 1)]['player_cards'] = player_cards
                player_info['player_hand ' + str(j + 1)]['player_sum'] = player_sum

                player_cards = player_info['player_hand ' + str(len(player_info))]['player_cards']
                player_cards, player_sum, cards_delt, bet, decision = player_hand_21_2(shuffle, cards_delt, player_cards, bet)
                player_info['player_hand ' + str(len(player_info))]['player_cards'] = player_cards
                player_info['player_hand ' + str(len(player_info))]['player_sum'] = player_sum

            while player_info['player_hand ' + str(j+1)]['player_sum'] < 21 and decision == '2':

                player_cards, player_sum, cards_delt, bet, decision = player_hand_21_2(shuffle, cards_delt, player_cards, bet)

                player_info['player_hand ' + str(j + 1)]['player_cards'] = player_cards
                player_info['player_hand ' + str(j + 1)]['player_sum'] = player_sum

            j += 1

        print('')
        dealer_sum, dealer_info, cards_delt = dealer_hand_s17(shuffle, cards_delt, dealer_info)
        player_won, dealer_won, bankroll = results(player_info, dealer_sum, player_won, dealer_won, bet, bankroll)

    print("")
    print("End of Shoe")
    return


game_21(1, 10000)
