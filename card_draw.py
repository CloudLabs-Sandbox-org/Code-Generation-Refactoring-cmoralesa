# Card drawing program

# importing modules
import itertools, random

# Dictionary for special cards
CARD_NAMES = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}

# make a deck of cards
deck = list(itertools.product(range(1,14), ['Spades','Hearts','Diamonds','Clubs']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("\nYou got:")
for i in range(5):
    number, suit = deck[i]
    # Convert number cards to special names (Ace, Jack, Queen, King)
    card_value = CARD_NAMES.get(number, str(number))
    print(f"{card_value} of {suit}")
