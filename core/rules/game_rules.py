import abc

class GameRules(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def isSnap(self, card, otherCard):
		"""
		Checks if two cards snap according to the rules this class represents.

		To be implemented by child class.

		:param card:
			A card being checked for snap.
		:param otherCard:
			The other card being checked for snap.
		:return:
			Boolean True if snap
		"""
		return
