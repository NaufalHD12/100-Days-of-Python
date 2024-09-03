from art import logo
import random
print(logo)
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


# print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if cards == [11, 10] or cards == [10, 11]:
        return 0
    for card in cards:
        if card == 11:
            if score > 21:
                cards.remove(11)
                cards.append(1)
    score = sum(cards)
    return score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You Lose😭"
    if user_score > 21:
        return "You went over. You Lose😭"
    if computer_score > 21:
        return "Computer went over. You Win😁"
    if user_score == computer_score:
        return "Draw🤔"
    if user_score == 0:
        return "Win with a Blackjack😎"
    if computer_score == 0:
        return "Computer has a Blackjack. You Lose😭"
    if user_score > computer_score:
        return "You Win😁"
    else:
        return "You Lose😭"


start_game = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while start_game == "y":
    user_cards = []
    computer_cards = []
    if start_game == "n":
        should_continue = False
    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(
        f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    game_over = False
    if user_score == 0 or computer_score == 0:
        game_over = True
        print(compare(user_score, computer_score))

    while not game_over:
        add_again = input("Type 'y' to get another card, type 'n' to pass: ")
        if add_again == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                game_over = True
        else:
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            game_over = True

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    start_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
