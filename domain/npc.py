import core.game as game
import random
from player import Player

class NPC(Player):
	minResponseTime = 0.5
	maxResponseTime = 3.0

	def __init__(self, stats):
		super(Player, self).__init__(stats["name"])
		self.speed = stats["speed"]
		self.accuracy = stats["accuracy"]

	def doMove(self, isSnap):
		if isSnap:
			# Generate a random response time modified by this NPCs speed
			self.snapResponseTime = random.uniform(NPC.minResponseTime, NPC.maxResponseTime) / self.speed
		else:
			# Snap anyway if this NPC misses
			if random.random() > self.accuracy:
				self.snapResponseTime = 1