from core.rules.game_rules import GameRules

class ValueOnlyRules(GameRules):
	def __init__(self):
		super(ValueOnlyRules, self).__init__()

	def isSnap(self, card, otherCard):
		"""
		Checks if two cards have the same value and thus a snap.

		:param card:
			First card.
		:param otherCard:
			Second card.
		:return:
			True if both cards have the same value, false otherwise.
		"""
		return card.value == otherCard.value
