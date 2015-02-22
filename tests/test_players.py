#!/usr/bin/python2.7

import unittest
from service.player_service import getNPCs
from domain.npc import NPC

class TestPlayers(unittest.TestCase):
	def testGetNpcs(self):
		numberOfNpcs = 7
		npcs = getNPCs(numberOfNpcs)
		self.failUnlessEqual(numberOfNpcs, len(npcs))

def main():
	unittest.main()

if __name__ == '__main__':
	main()