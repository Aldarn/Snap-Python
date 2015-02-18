import random
import itertools

SUITS = 'hdcs'
VALUES = 'A23456789TJQK'

def getDeck(numberOfPacks, shuffled = True):
	"""
	Gets the deck using the number of packs specified.

	:param numberOfPacks:
		The number of packs desired to comprise the deck.
	:param shuffled:
		Boolean toggle to shuffle the deck before returning.
	:return:
		The deck as a list of two character strings representing the cards.
	"""
	deck = []
	for n in range(numberOfPacks):
		deck.extend([''.join(card) for card in itertools.product(VALUES, SUITS)])

	return random.shuffle(deck) if shuffled else deck
