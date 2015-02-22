import random
import itertools

from domain.card import Card

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
		deck.extend([Card(''.join(card)) for card in itertools.product(Card.VALUES.keys(), Card.SUITS.keys())])

	if shuffled:
		shuffle(deck)

	return deck

def shuffle(deck):
	"""
	Shuffles the deck.

	:param deck:
		The deck to shuffle.
	"""
	random.shuffle(deck)

def isValidNumberOfPacks(numberOfPacks):
	"""
	Checks if the number of packs is valid.

	:param numberOfPacks:
		The number to check.
	:return:
		True if valid, false otherwise.
	"""
	return 0 < numberOfPacks < 101
