'''
Day 11: Blackjack game

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
'''
import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0;
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):
    user_score = calc_score(user)
    computer_score = calc_score(computer)
    if user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("It is a tie.")
    else:
        print("You lose.")

def game():

    #deal hands for players
    user_hand = []
    computer_hand = []
    is_game = True

    for i in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    #check for blackjack
    user_score = calc_score(user_hand)
    computer_score = calc_score(computer_hand)
    if user_score == 0 and computer_score == 0:
        is_game = False
        print("The game is a tie, both player and dealer have blackjack!")
    elif user_score == 0:
        is_game = False
        print("You win, you got blackjack!")
    elif computer_score == 0:
        is_game = False
        print("You lose, the computer got blackjack.")

    #game logic
    while is_game:
        user_score = calc_score(user_hand)
        if user_score > 21:
            is_game = False
            print("You busted.")
            break
        #computer_score = calc_score(computer_hand)
        print(f"Your hand: {user_hand}, score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        if input("Would you like another card? y/n") == 'y':
            user_hand.append(deal_card())
        else:
            is_game = False


