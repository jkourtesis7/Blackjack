"""
Blackjack program
"""

import random
import time

def main():
    #Print - welcome
    print('Welcome to Blackjack')

    play = 'y'

    while play == 'y':
        time.sleep(1)
        #invite to play
        play = input('Do you wish to start a new game? (y/n):')

        #Exit on no.
        if play.upper().startswith('N'):
            print('See you next time!')
            exit()
        #Call Game on yes
        if play.upper().startswith('Y'):
            play_game()
        #Ask again if entry invalid
        else:
            print('Invalid Entry')
            play = 'y'
            continue


def play_game():
    #Deal Initial hands
    dealer_hand = initial_cards()
    player_hand = initial_cards()
    #Present Initial Cards
    time.sleep(1)
    print(f'You draw a {player_hand[0]} and a {player_hand[1]}')
    time.sleep(1)
    print(f'Your total is {sum_hand(player_hand)}')
    time.sleep(1)
    print(f'The Dealer drew {dealer_hand[0]} and a hidden card')

    #Run Player turn
    player_hand = playturn('player',player_hand)
    if sum_hand(player_hand) > 21:
        print('Busted!! Better luck next time')
        return
    time.sleep(1)
    print('You Stand')

    #Run Dealer's turn
    dealer_hand = playturn('dealer',dealer_hand)
    if sum_hand(dealer_hand) > 21:
        time.sleep(1)
        print(' The Dealer Busted!! You Win!!')
        return
    time.sleep(1)
    print('The dealer stands.')

    #Calc and present totals
    player_total = sum_hand(player_hand)
    dealer_total = sum_hand(dealer_hand)
    time.sleep(1)
    print(f'Your total is {player_total} and the dealers total is {dealer_total}')

    #Determine Winner
    if sum_hand(dealer_hand) >= sum_hand(player_hand):
        time.sleep(1)
        print('The dealer wins!')

    else:
        time.sleep(1)
        print('You win!')


def playturn(turn, hand):
    active_hand = hand
    action = 'h'

    #Player turn sequence
    if turn == 'player':
        while action == 'h':
            time.sleep(1)
            action = input('Hit or stand? (h/s): ')
            if action.upper().startswith('S'):
                break
            if action.upper().startswith('H'):
                active_hand.append(delt_card())
                time.sleep(1)
                print(f'Hit! You drew a {active_hand[-1]}. Your total is {sum_hand(active_hand)}.')
                action ='h'
                if sum_hand(active_hand) > 20:
                    break
            else:
                print('Invalid Entry')
                action = 'h'
                continue

    #Dealer Turn Sequence
    if turn == 'dealer':
        time.sleep(1)
        print(f'The dealer reveals the hidden card of {active_hand[-1]}, and has a total of {sum_hand(active_hand)}.')
        while sum_hand(active_hand) < 17:
            active_hand.append(delt_card())
            time.sleep(1)
            print(f"Hit! The dealer draws {active_hand[-1]}. The dealer's total is {sum_hand(active_hand)}.")


    #print(f'{active_turn} and {active_hand}')
    return active_hand

def sum_hand(hand):
    #Hand totaling function
    total = int(0)
    for card in hand:
        total += int(card)
    return total

def initial_cards():
    #Initial card deal
    starting_hand = list()
    while len(starting_hand) < 2:
        starting_hand.append(delt_card())
    return starting_hand

def delt_card():
    #Deal another card
    card = random.randint(1, 10)
    return card

if __name__ == '__main__': main()
