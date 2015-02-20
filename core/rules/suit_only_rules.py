from core.rules.game_rules import GameRules

class SuitOnlyRules(GameRules):
	def __init__(self):
		super(SuitOnlyRules, self).__init__()

	def isSnap(self, card, otherCard):
		"""
		Checks if two cards have the same suit and thus a snap.

		:param card:
		:param otherCard:
		:return:
		"""
		# TODO
		return True
