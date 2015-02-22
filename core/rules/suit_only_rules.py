from core.rules.game_rules import GameRules

class SuitOnlyRules(GameRules):
	def __init__(self):
		super(SuitOnlyRules, self).__init__()

	def isSnap(self, card, otherCard):
		"""
		Checks if two cards have the same suit and thus a snap.

		:param card:
			First card.
		:param otherCard:
			Second card.
		:return:
			True if both cards have the same suit, false otherwise.
		"""
		return card.suit == otherCard.suit
