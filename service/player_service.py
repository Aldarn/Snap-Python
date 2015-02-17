from domain.npc import NPC
import resources.resources as resources
import json

npcs = json.loads(resources.getResourcePath("npcs.json"))

def getNPCs(numberOfNPCs):
	return [NPC(npcs.pop()) for n in range(0, numberOfNPCs)]