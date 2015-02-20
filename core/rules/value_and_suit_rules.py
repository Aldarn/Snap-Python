from core.rules.game_rules import GameRules

class ValueAndSuitRules(GameRules):
	def __init__(self):
		super(ValueAndSuitRules, self).__init__()

	def isSnap(self, card, otherCard):
		"""
		Checks if two cards have the same suit or value and thus a snap.

		:param card:
		:param otherCard:
		:return:
		"""
		# TODO
		return True
