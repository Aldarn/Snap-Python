from domain.npc import NPC
import resources.resources as resources

import simplejson
import random

NPCS = simplejson.load(open(resources.getResourcePath("npcs.json"), 'r'))

def getNPCs(numberOfNPCs):
	"""
	Gets a list of a chosen number of randomly selected NPCs.

	:param numberOfNPCs:
		The number of NPCs to get.
	:return:
		List of random NPCs.
	"""
	return [NPC(npc) for npc in random.sample(NPCS, numberOfNPCs)]

def isValidNumberOfPlayers(numberOfPlayers):
	"""
	Checks if the number of players is valid.

	:param numberOfPlayers:
		The number to check.
	:return:
		True if valid, false otherwise.
	"""
	return 1 < numberOfPlayers < 11
