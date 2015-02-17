import abc
import core.game as game

class Player(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, name):
		self.name = name
		self.snapResponseTime = -1

	@abc.abstractmethod
	def doMove(self, isSnap):
		"""
		Performs a move for the player in response to the latest card flipped.

		:param isSnap:
			Boolean whether the game is in a snap state or not.
		"""
		return

	#####################
	# 	  Properties	#
	#####################

	def getSnapResponseTime(self):
		return self.snapResponseTime

	def setSnapResponseTime(self, snapResponseTime):
		self.snapResponseTime = snapResponseTime

	snapResponseTime = property(getSnapResponseTime, setSnapResponseTime, doc = "I'm the 'x' property.")
