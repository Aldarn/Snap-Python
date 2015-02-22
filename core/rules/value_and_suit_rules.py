from core.rules.suit_only_rules import SuitOnlyRules
from core.rules.value_only_rules import ValueOnlyRules

class ValueAndSuitRules(SuitOnlyRules, ValueOnlyRules):
	def __init__(self):
		SuitOnlyRules.__init__(self)
		ValueOnlyRules.__init__(self)

	def isSnap(self, card, otherCard):
		"""
		Checks if two cards have the same suit or value and thus a snap.

		:param card:
			First card.
		:param otherCard:
			Second card.
		:return:
			True if the cards snap under either of the other two rules, false otherwise.
		"""
		return SuitOnlyRules.isSnap(self, card, otherCard) or ValueOnlyRules.isSnap(self, card, otherCard)
