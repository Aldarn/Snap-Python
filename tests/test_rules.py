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
		card = Card("jh")
		otherCard = Card("jc")
		self.failUnless(valueRules.isSnap(card, otherCard))

	def testValueNoSnap(self):
		valueRules = ValueOnlyRules()
		card = Card("kh")
		otherCard = Card("2h")
		self.failIf(valueRules.isSnap(card, otherCard))

	def testSuitSnap(self):
		suitRules = SuitOnlyRules()
		card = Card("td")
		otherCard = Card("6d")
		self.failUnless(suitRules.isSnap(card, otherCard))

	def testSuitNoSnap(self):
		suitRules = SuitOnlyRules()
		card = Card("3s")
		otherCard = Card("3c")
		self.failIf(suitRules.isSnap(card, otherCard))

	def testBothSnap(self):
		bothRules = ValueAndSuitRules()
		card = Card("kd")
		otherCard = Card("kc")
		card2 = Card("7s")
		otherCard2 = Card("as")

		self.failUnless(bothRules.isSnap(card, otherCard))
		self.failUnless(bothRules.isSnap(card2, otherCard2))

	def testBothNoSnap(self):
		bothRules = ValueAndSuitRules()
		card = Card("qc")
		otherCard = Card("as")
		self.failIf(bothRules.isSnap(card, otherCard))

def main():
	unittest.main()

if __name__ == '__main__':
	main()