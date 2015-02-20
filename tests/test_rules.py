#!/usr/bin/python2.7

import unittest
from service.rules_service import getRulesFromInput
from core.rules.suit_only_rules import SuitOnlyRules
from core.rules.value_only_rules import ValueOnlyRules
from core.rules.value_and_suit_rules import ValueAndSuitRules

class TestDealer(unittest.TestCase):
	def testGetValueOnlyRules(self):
		rules = getRulesFromInput("value")
		self.failUnless(isinstance(rules, ValueOnlyRules))

	def testGetSuitOnlyRules(self):
		rules = getRulesFromInput("suit")
		self.failUnless(isinstance(rules, SuitOnlyRules))

	def testGetBothRules(self):
		rules = getRulesFromInput("both")
		self.failUnless(isinstance(rules, ValueAndSuitRules))

def main():
	unittest.main()

if __name__ == '__main__':
	main()