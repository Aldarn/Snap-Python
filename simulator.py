#!/usr/bin/python2.7

import core.game as game
import core.dealer as dealer
import service.player_service as playerService
import service.rules_service as ruleService

def getNumberOfDecks():
	try:
		return int(raw_input("How many decks would you like to play with? "))
	except ValueError:
		return -1

def getNumberOfPlayers():
	try:
		return int(raw_input("How many players would you like to play with (max 10)? "))
	except:
		return -1

def getGameRules():
	return raw_input("Which rules of the game would you like to play (" + ", ".join(ruleService.RULES.keys()) + ")? ")

def main():
	print "Welcome to digital Snap!\n"

	# Request number of decks
	numberOfDecks = getNumberOfDecks()
	while numberOfDecks < 1 or numberOfDecks > 100:
		print "Please choose a number > 0 and < 101"
		numberOfDecks = getNumberOfDecks()

	# Request number of players
	numberOfPlayers = getNumberOfPlayers()
	while numberOfPlayers < 2 or numberOfPlayers > 10:
		print "Please choose a number > 1 and < 11"
		numberOfPlayers = getNumberOfPlayers()

	# Request number of players
	gameRules = ruleService.getRulesFromInput(getGameRules())
	while gameRules is None:
		print "Please choose from the following:\n" + "\n".join(ruleService.RULES.keys())
		gameRules = ruleService.getRulesFromInput(getGameRules())

	# Start the simulation
	# TODO: Should these be passed as args?
	game.DECK = dealer.getDeck(numberOfDecks)
	game.PLAYERS = playerService.getNPCs(numberOfPlayers)
	game.RULES = gameRules
	game.start()

if __name__ == '__main__':
	main()
