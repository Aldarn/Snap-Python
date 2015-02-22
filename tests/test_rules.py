#!/usr/bin/python2.7

import unittest
from domain.card import Card
from service.rules_service import getRulesFromInput
from core.rules.suit_only_rules import SuitOnlyRules
from core.rules.value_only_rules import ValueOnlyRules
from core.rules.value_and_suit_rules import ValueAndSuitRules

class TestRules(unittest.TestCase):
	def testGetValueOnlyRules(self):
		rules = getRulesFromInput("value")
		self.failUnless(isinstance(rules, ValueOnlyRules))

	def testGetSuitOnlyRules(self):
		rules = getRulesFromInput("suit")
		self.failUnless(isinstance(rules, SuitOnlyRules))

	def testGetBothRules(self):
		rules = getRulesFromInput("both")
		self.failUnless(isinstance(rules, ValueAndSuitRules))

	def testValueSnap(self):
		valueRules = ValueOnlyRules()
		card = Card("j", "h")
		otherCard = Card("j", "c")
		self.failUnless(valueRules.isSnap(card, otherCard))

	def testValueNoSnap(self):
		valueRules = ValueOnlyRules()
		card = Card("k", "h")
		otherCard = Card("2", "h")
		self.failIf(valueRules.isSnap(card, otherCard))

	def testSuitSnap(self):
		suitRules = SuitOnlyRules()
		card = Card("t", "d")
		otherCard = Card("6", "d")
		self.failUnless(suitRules.isSnap(card, otherCard))

	def testSuitNoSnap(self):
		suitRules = SuitOnlyRules()
		card = Card("3", "s")
		otherCard = Card("3", "c")
		self.failIf(suitRules.isSnap(card, otherCard))

	def testBothSnap(self):
		bothRules = ValueAndSuitRules()
		card = Card("k", "d")
		otherCard = Card("k", "c")
		card2 = Card("7", "s")
		otherCard2 = Card("a", "s")

		self.failUnless(bothRules.isSnap(card, otherCard))
		self.failUnless(bothRules.isSnap(card2, otherCard2))

	def testBothNoSnap(self):
		bothRules = ValueAndSuitRules()
		card = Card("q", "c")
		otherCard = Card("a", "s")
		self.failIf(bothRules.isSnap(card, otherCard))

def main():
	unittest.main()

if __name__ == '__main__':
	main()