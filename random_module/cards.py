# Add imports here
import random

# Complete the function
#write a function that takes as arguments a list of suits and a list of ranks. Inside the function create the list of the deck and return a random group of 4 cards.

def cards_sample(suits, ranks):
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return random.sample(deck, 4)

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King']

print(cards_sample(suits, ranks))
