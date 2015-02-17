#!/usr/bin/python2.7

import core.game as game
import core.dealer as dealer
import service.player_service as playerService

def main():
	print "Welcome to digital Snap!\n\n"

	# Request number of decks
	numberOfDecks = raw_input("How many decks would you like to play with? ")

	# Request number of players
	numberOfPlayers = raw_input("How many players would you like to play with (max 10)? ")

	# Start the simulation
	game.start(dealer.getDeck(numberOfDecks), playerService.getNPCs(numberOfPlayers))

if __name__ == '__main__':
	main()
