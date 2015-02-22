import random
import itertools

from domain.card_types import VALUES, SUITS
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
		deck.extend([Card(card[0], card[1]) for card in itertools.product(VALUES.keys(), SUITS.keys())])

	if shuffled:
		random.shuffle(deck)

	return deck

def isValidNumberOfPacks(numberOfPacks):
	"""
	Checks if the number of packs is valid.

	:param numberOfPacks:
		The number to check.
	:return:
		True if valid, false otherwise.
	"""
	return 0 < numberOfPacks < 101
