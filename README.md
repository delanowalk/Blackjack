# Blackjack

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:09:58 2023

@author: dwalker

#Runs black Jack game

"""

    from random import randint
    import numpy as np
    from numpy import ndarray


    def deck_amount(decks: object) -> object:
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

"""
Defines the deck and the values for each card two slots cause Aces suck
"""

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
                print("Cards shuffled")
        return shuffle

"""
Creates the shuffle as an array that we will count though
"""

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

"""
sum for array, edge cases and not greater then 21
"""

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

"""
counting cards
"""

    def hand_21(shuffle, deck, cards_delt):

        dealer_info: ndarray = np.array([])
        player_info: ndarray = np.array([])

        dealer_sum = 0
        dealer_card1 = shuffle[cards_delt]
        cards_delt += 1
        dealer_card2 = shuffle[cards_delt]
        cards_delt += 1
        dealer_sum = deck[dealer_card1][1] + deck[dealer_card2][1]

        player_sum = 0
        player_card1 = shuffle[cards_delt]
        cards_delt += 1
        player_card2 = shuffle[cards_delt]
        cards_delt += 1
        player_sum = deck[player_card1][1] + deck[player_card2][1]

        if deck[player_card1][1] == 11 and deck[player_card2][1] == 11:
         player_sum = deck[player_card1][1] + deck[player_card2][2]

        player_info = np.append(player_info, player_card1)
        player_info = np.append(player_info, player_card2)

        dealer_info = np.append(dealer_info, dealer_card1)
        dealer_info = np.append(dealer_info, dealer_card2)

        print(f"dealer card 1    : {dealer_info[0]}")
        print(f"player cards     : {player_info[0], player_info[1]}")
        print(f"player sum       : {player_sum}")

        while player_sum <= 21:
            hit = input("hit yes or no?")
            if hit == 'y':
                player_hit_card = shuffle[cards_delt]
                cards_delt += 1
                player_info = np.append(player_info, player_hit_card)
                player_sum = sum_cards(player_info)

                print(f'player Hit Card   : {player_hit_card}')
                print(f'player sum        : {player_sum}')

                if player_sum > 21:
                    print('player busted')
                    print("Dealer won")
                    print(f'dealer card 1     : {dealer_card1}')
                    print(f'dealer card 2     : {dealer_card2}')
                    return cards_delt, player_info, dealer_info

            if hit == 'n':
                print(f'dealer cards      : {dealer_card1, dealer_card2}')
                print(f'dealer sum        : {dealer_sum}')
                while dealer_sum < 17:
                    dealer_hit_card = shuffle[cards_delt]
                    cards_delt += 1
                    dealer_info = np.append(dealer_info, dealer_hit_card)
                    dealer_sum = sum_cards(dealer_info)

                    print(f'dealer hit card   : {dealer_hit_card}')
                    print(f'dealer sum        : {dealer_sum}')

                    if dealer_sum > 21:
                        print('dealer bust')
                        print('player won')
                        return cards_delt, player_info, dealer_info

                if dealer_sum > player_sum:
                    print(f'player sum        : {player_sum}')
                    print(f'dealer sum        : {dealer_sum}')
                    print('dealer won')
                    return cards_delt, player_info, dealer_info

                elif player_sum > dealer_sum:
                    print(f'dealer cards      : {dealer_card1, dealer_card2}')
                    print(f'dealer sum        : {dealer_sum}')
                    print(f'player sum        : {player_sum}')
                    print('player won')
                    return cards_delt, player_info, dealer_info

                elif player_sum == dealer_sum:
                    print(f'dealer cards      : {dealer_card1, dealer_card2}')
                    print(f'dealer sum        : {dealer_sum}')
                    print(f'player sum        : {player_sum}')
                    print('push')
                    return cards_delt, player_info, dealer_info

                else:
                    print('shit Idk')
                    return


    def game_21(amount_of_decks):
        shuffle = shoe(amount_of_decks)
        deck = deck_amount(amount_of_decks)
        cards_delt = 0
        high_low_count = 0
        while cards_delt < (len(shuffle) - randint(10, 20)):
            decks_left = (len(shuffle) - cards_delt) / 52
            high_low_count = counting_card(cards_delt, shuffle)
            true_count = high_low_count/decks_left

            print("")
            print(f'Cards Delt     :{cards_delt}')
            print(f'Decks Left     :{decks_left}')
            print(f'Running Count  :{high_low_count}')
            print(f'True Count     :{true_count}')
            print("")
            print("New Hand")

            cards_delt = hand_21(shuffle, deck, cards_delt)[0]
        print("End of Shoe")
        return


    game_21(2)


