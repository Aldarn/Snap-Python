#!/usr/bin/python2.7

import unittest
from core.dealer import getDeck

class TestDealer(unittest.TestCase):
	def testDeckIsFull(self):
		numberOfPacks = 1
		deck = getDeck(numberOfPacks)
		self.failUnlessEqual(len(deck), 52)

	def testMultiplePacks(self):
		numberOfPacks = 3
		deck = getDeck(numberOfPacks, shuffled = False)
		self.failUnlessEqual(len(deck), 52 * numberOfPacks)

	def testDeckIsShuffled(self):
		# High number to prevent the chance of the shuffle returning them in the same order as they're created
		# TODO: This should be improved using mocks and verifying the shuffle is called
		numberOfPacks = 10
		shuffledDeck = getDeck(numberOfPacks, shuffled = True)
		deck = getDeck(numberOfPacks, shuffled = False)
		self.failIfEqual(shuffledDeck, deck)

def main():
	unittest.main()

if __name__ == '__main__':
	main()