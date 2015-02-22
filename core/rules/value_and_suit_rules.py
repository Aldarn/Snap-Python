from core.rules.game_rules import GameRules
from core.rules.suit_only_rules import SuitOnlyRules
from core.rules.value_only_rules import ValueOnlyRules

class ValueAndSuitRules(GameRules):
	def __init__(self):
		super(ValueAndSuitRules, self).__init__()
		self.suitOnlyRules = SuitOnlyRules()
		self.valueOnlyRules = ValueOnlyRules()

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
		return self.suitOnlyRules.isSnap(card, otherCard) or self.valueOnlyRules.isSnap(card, otherCard)
