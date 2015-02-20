from domain.npc import NPC
import resources.resources as resources
import simplejson

npcs = simplejson.load(open(resources.getResourcePath("npcs.json"), 'r'))

def getNPCs(numberOfNPCs):
	return [NPC(npcs.pop()) for n in range(0, numberOfNPCs)]