import abc

class Player(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, name):
		self._name = name
		self._snapResponseTime = -1
		self._cards = []

	@abc.abstractmethod
	def doMove(self, isSnap):
		"""
		Performs a move for the player in response to the latest card flipped.

		To be implemented by child class.

		:param isSnap:
			Boolean whether the game is in a snap state or not.
		"""
		return

	def addCards(self, cards):
		"""
		Adds the given cards to the players hand.

		:param cards:
			The cards to add.
		"""
		self._cards.extend(cards)

	def removeCards(self, count):
		"""
		Removes a given number of cards from the players hand.

		:param count:
			The number of cards to remove.
		"""
		try:
			del self._cards[-count:]
		except IndexError:
			self.resetHand()

	def getCardCount(self):
		"""
		Gets the number of cards in the players hand.

		:return:
			Number of cards in the players hand.
		"""
		return len(self._cards)

	def resetHand(self):
		"""
		Empties the list of cards in this players hand.
		"""
		del self._cards[:]

	@property
	def name(self):
		return self._name

	@property
	def snapResponseTime(self):
		return self._snapResponseTime

	@snapResponseTime.setter
	def snapResponseTime(self, snapResponseTime):
		self._snapResponseTime = snapResponseTime
