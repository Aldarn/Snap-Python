from core.rules.game_rules import GameRules

class ValueOnlyRules(GameRules):
	def __init__(self):
		super(ValueOnlyRules, self).__init__()

	def isSnap(self, card, otherCard):
		"""
		Checks if two cards have the same value and thus a snap.

		:param card:
		:param otherCard:
		:return:
		"""
		# TODO
		return True
