from typing import Any

import art
import random
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    print(art.logo)
    game_over = False
    another_card = ''
    while not game_over:
        print(f"Dealing 2 cards to you and the computer")
        user_cards, dealer_cards = initial_deal_cards()
        print(f"You have {user_cards}. Current score is {sum(user_cards)}")
        print(f"The dealer is showing {dealer_cards[0]}")
        if sum(user_cards) == 21:
            print(f"BLACKJACK! You win!")
            game_over = True
        else:
            while another_card != 'n' and not game_over:
                another_card = input("Type 'y' for another card, type 'n' to pass: ")
                if another_card == 'y':
                    user_deal_card(user_cards, dealer_cards)
                    user_cards, dealer_cards, game_over = calculate_score(user_cards, dealer_cards, game_over)
                else:
                    dealer_cards = dealer_deal_card(user_cards, dealer_cards)
                    game_over = winning_losing(user_cards, dealer_cards, game_over)

def deal_card():
    return random.choice(cards)

def initial_deal_cards():
    user_cards = []
    dealer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
    dealer_cards.append(deal_card())
    # user_cards = [2,11]
    # dealer_cards = [9,9]
    print(f"{user_cards} and {dealer_cards}")
    return user_cards, dealer_cards

def user_deal_card(user_cards, dealer_cards):
    user_cards.append(deal_card())
    print(f"{user_cards} and {dealer_cards}")
    return user_cards

def dealer_deal_card(user_cards, dealer_cards):
    print(f"{dealer_cards}")
    while sum(dealer_cards) < 17:
        if sum(dealer_cards) > 21:
            for card in dealer_cards:
                if card == 11:
                    dealer_cards.remove(card)
                    dealer_cards.append(1)
                    print(dealer_cards)
        else:
            dealer_cards.append(deal_card())
            print(f"{user_cards} and {dealer_cards}")
    return dealer_cards

#dealer_deal_card([8,11] , [10,5])

def calculate_score(user_cards, dealer_cards, game_over):
    print(sum(user_cards))
    if sum(user_cards) > 21:
        print(f"this is working")
        for card in user_cards:
            if card == 11:
                user_cards.remove(card)
                user_cards.append(1)
                print(user_cards)
        if sum(user_cards) > 21:
            print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
            print("You busted! NUTTTTT")
            game_over = True
        else:
            print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
    else:
        print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
    return user_cards, dealer_cards, game_over

def winning_losing(user_cards, dealer_cards, game_over):
    if sum(user_cards) == sum(dealer_cards):
        print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
        print('It''s a push!')
    elif sum(dealer_cards) > 21:
        print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
        print(f"Dealer Busted. You WIN!")
    elif sum(user_cards) > sum(dealer_cards):
        print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
        print('You win!')
    else:
        print(f"User Cards {user_cards} \nDealer Cards {dealer_cards}")
        print('You lose SADDDDD')
    game_over = True
    return game_over



#calculate_score([11, 15], [9, 9], False)

#blackjack()
abg = True
while abg:
    blackjack()