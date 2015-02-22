#!/usr/bin/python2.7

import unittest
from service.player_service import getNPCs
from domain.npc import NPC
from domain.card import Card

class TestPlayers(unittest.TestCase):
	def testGetNpcs(self):
		numberOfNpcs = 7
		npcs = getNPCs(numberOfNpcs)
		self.failUnlessEqual(numberOfNpcs, len(npcs))

	def testAddCards(self):
		cardsToAdd = [Card("a", "h"), Card("4", "s")]
		npc = getNPCs(1)[0]
		npc.addCards(cardsToAdd)
		self.failUnlessEqual(cardsToAdd, npc._cards)

	def testRemoveCards(self):
		cardsToRemove = 2
		cards = [Card("a", "h"), Card("4", "s"), Card("7", "c")]
		npc = getNPCs(1)[0]
		npc.addCards(cards)
		npc.removeCards(cardsToRemove)
		self.failUnlessEqual(cards[0:1], npc._cards)

	def testRemoveTooManyCards(self):
		cardsToRemove = 2
		cards = [Card("a", "h")]
		npc = getNPCs(1)[0]
		npc.addCards(cards)
		npc.removeCards(cardsToRemove)
		self.failUnlessEqual([], npc._cards)

	def testCountCards(self):
		npc = getNPCs(1)[0]
		npc.addCards([Card("a", "h"), Card("4", "s")])
		self.failUnlessEqual(2, npc.getCardCount())

	def testResetHand(self):
		npc = getNPCs(1)[0]
		npc.addCards([Card("a", "h"), Card("4", "s")])
		npc.resetHand()
		self.failUnlessEqual([], npc._cards)

	def testNPCDoMoveSnap(self):
		npc = NPC({"name": "test", "speed": 1.0, "accuracy": 1.0})
		npc.doMove(True)
		self.failUnless(npc.snapResponseTime > 0)

	def testNPCDoMoveIsSnap(self):
		npc = NPC({"name": "test", "speed": 1.0, "accuracy": 1.0})
		npc.doMove(True)
		self.failUnless(npc.snapResponseTime > 0)

	def testNPCDoMoveNoSnapNoMiss(self):
		npc = NPC({"name": "test", "speed": 1.0, "accuracy": 1.0})
		npc.snapResponseTime = 1
		npc.doMove(False)
		self.failUnless(npc.snapResponseTime < 0)

	def testNPCDoMoveNoSnapMiss(self):
		npc = NPC({"name": "test", "speed": 1.0, "accuracy": 0.0})
		npc.doMove(False)
		self.failUnless(npc.snapResponseTime > 0)

def main():
	unittest.main()

if __name__ == '__main__':
	main()