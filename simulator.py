#!/usr/bin/python2.7

from core.game import Game
import service.card_service as cardService
import service.player_service as playerService
import service.rules_service as ruleService

import argparse

def getNumberOfPacks():
	try:
		numberOfPacks = int(raw_input("How many packs would you like to play with? "))
		if not cardService.isValidNumberOfPacks(numberOfPacks):
			raise ValueError("Invalid number of packs chosen.")
		return numberOfPacks
	except ValueError:
		print "Please choose a number > 0 and < 101"
		return getNumberOfPacks()

def getNumberOfPlayers():
	try:
		numberOfPlayers = int(raw_input("How many players would you like to play with (max 10)? "))
		if not playerService.isValidNumberOfPlayers(numberOfPlayers):
			raise ValueError("Invalid number of players chosen.")
		return numberOfPlayers
	except ValueError:
		print "Please choose a number > 1 and < 11"
		return getNumberOfPlayers()

def getGameRules():
	rules = ruleService.getRulesFromInput(
		raw_input("Which rules of the game would you like to play (" + ", ".join(ruleService.RULES.keys()) + ")? ")
	)
	if rules is None:
		print "Please choose from the following:\n" + "\n".join(ruleService.RULES.keys())
		return getGameRules()
	return rules

def getCommandLineArguments():
	parser = argparse.ArgumentParser(description="Play a game of Snap!")
	parser.add_argument("-p", "--packs", type = int, dest = "numberOfPacks",
		default = 0, help = "The number of packs to play with.")
	parser.add_argument("-pl", "--players", type = int, dest = "numberOfPlayers",
		default = 0, help = "The number of players to play with.")
	parser.add_argument("-r", "--rules", type = str, dest = "gameRules", default = None,
		choices = ruleService.RULES.keys(), help = "The rules to play with.")

	args = parser.parse_args()
	if args.gameRules is not None:
		args.gameRules = ruleService.getRulesFromInput(args.gameRules)
	return args

def main():
	print "Welcome to digital Snap!\n"

	# Get any command line arguments supplied
	commandLineArguments = getCommandLineArguments()

	# Request number of decks
	numberOfPacks = commandLineArguments.numberOfPacks \
		if cardService.isValidNumberOfPacks(commandLineArguments.numberOfPacks) else getNumberOfPacks()

	# Request number of players
	numberOfPlayers = commandLineArguments.numberOfPlayers \
		if playerService.isValidNumberOfPlayers(commandLineArguments.numberOfPlayers) else getNumberOfPlayers()

	# Request number of players
	gameRules = commandLineArguments.gameRules if commandLineArguments.gameRules is not None else getGameRules()

	# Start the simulation
	game = Game(numberOfPacks, playerService.getNPCs(numberOfPlayers), gameRules)
	game.run()

if __name__ == '__main__':
	main()
