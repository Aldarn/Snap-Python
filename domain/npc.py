import core.game as game
import random
from player import Player

class NPC(Player):
	minResponseTime = 0.5
	maxResponseTime = 3.0

	def __init__(self, stats):
		super(Player, self).__init__()
		self._speed = stats["speed"]
		self._accuracy = stats["accuracy"]

	def doMove(self, isSnap):
		if isSnap:
			# Generate a random response time modified by this NPCs speed
			self.snapResponseTime = random.uniform(NPC.minResponseTime, NPC.maxResponseTime) / self._speed
		else:
			# Snap anyway if this NPC misses
			if random.random() > self._accuracy:
				self.snapResponseTime = 1
			# Reset the snap response time
			else:
				self.snapResponseTime = -1

	@property
	def speed(self):
		return self._speed

	@property
	def accuracy(self):
		return self._accuracy
