#!/usr/bin/python2.7

import unittest
import sys

from core.game import Game
from core.rules.value_and_suit_rules import ValueAndSuitRules
from service.player_service import getNPCs
from domain.card import Card

class TestGame(unittest.TestCase):
	def setUp(self):
		self.stdout = sys.stdout
		sys.stdout = TestStdout()
		self.game = Game(1, getNPCs(2), ValueAndSuitRules())

	def tearDown(self):
		sys.stdout = self.stdout

	def testInit(self):
		self.failUnlessEqual(len(self.game.deck), 52)
		self.failUnlessEqual(len(self.game.pot), 0)

	def testRun(self):
		self.game._run(lambda: "")
		self.failUnlessEqual(len(self.game.deck), 0)

	def testProcessSnap(self):
		pot = [Card("2", "h"), Card("j", "c")]
		self.game.players[0].snapResponseTime = 1
		self.game.players[1].snapResponseTime = 2
		self.game.pot = pot[:]
		self.game.processSnap()
		self.failUnlessEqual(self.game.players[0]._cards, pot)
		self.failUnlessEqual(self.game.players[1]._cards, [])
		self.failUnlessEqual(len(self.game.pot), 0)

	def testProcessNoSnap(self):
		cards = [Card("2", "h"), Card("j", "c"), Card("a", "s")]
		self.game.players[0].snapResponseTime = 1
		self.game.players[0]._cards = cards
		self.game.processNoSnap()
		self.failUnlessEqual(self.game.players[0]._cards, cards[0:1])

	def testAnnounceWinner(self):
		cards = [Card("2", "h")]
		self.game.players[0]._cards = cards
		self.game._announceWinner(lambda: "")
		self.failUnless("%s won the game with %i cards!" % (self.game.players[0].name, len(cards)) in TestStdout.written)

	def testAnnounceWinnerDraw(self):
		cards = [Card("2", "h")]
		self.game.players[0]._cards = cards
		self.game.players[1]._cards = cards
		self.game._announceWinner(lambda: "")
		self.failUnless("%s drew the game with %i cards each!"
			% (' & '.join([player.name for player in self.game.players]), len(cards)) in TestStdout.written)

	def testCheckRematch(self):
		cards = [Card("2", "h")]
		cards2 = [Card("a", "s")]
		self.game.players[0]._cards = cards[:]
		self.game.players[1]._cards = cards2[:]
		self.game._checkRematch(lambda: True, lambda: "")
		self.failUnlessEqual(self.game.players[0]._cards, [])
		self.failUnlessEqual(self.game.players[1]._cards, [])
		self.failUnlessEqual(len(self.game.deck), 52)
		self.failUnlessEqual(self.game.pot, [])

class TestStdout(object):
	"""
	Used to swallow stdout whilst testing. Serves the dual purpose of preventing terminal spam and allowing
	brittle tests against printed output.
	"""
	written = ""
	def write(self, s):
		TestStdout.written += s

def main():
	unittest.main()

if __name__ == '__main__':
	main()
