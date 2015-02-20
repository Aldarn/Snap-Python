import abc
import core.game as game

class Player(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, name):
		self.name = name
		self._snapResponseTime = -1

	@abc.abstractmethod
	def doMove(self, isSnap):
		"""
		Performs a move for the player in response to the latest card flipped.

		To be implemented by child class.

		:param isSnap:
			Boolean whether the game is in a snap state or not.
		"""
		return

	#####################
	# 	  Properties	#
	#####################

	@property
	def snapResponseTime(self):
		return self._snapResponseTime

	@snapResponseTime.setter
	def snapResponseTime(self, snapResponseTime):
		self._snapResponseTime = snapResponseTime
