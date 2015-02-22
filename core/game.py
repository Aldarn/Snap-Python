import service.card_service as cardService

NUMBER_OF_PACKS = 0
DECK = None
PLAYERS = None
RULES = None

# The pot holds the current cards that have been played
POT = []

def start(numberOfPacks, players, gameRules):
	"""
	Initializes the game and begins the match.

	:param deck:
		The deck.
	:param players:
		The players.
	:param gameRules:
		The game rules.
	"""
	global NUMBER_OF_PACKS, DECK, PLAYERS, RULES
	NUMBER_OF_PACKS = numberOfPacks
	DECK = cardService.getDeck(NUMBER_OF_PACKS)
	PLAYERS = players
	RULES = gameRules

	run()

def run():
	"""
	The main game loop that plays out each round.
	"""
	# Keep going until there's no deck left
	while len(DECK) > 0:
		card = DECK.pop()
		print "The dealer turned the %s" % card
		POT.append(card)

		# Skip this round if this is the first card in the current pot (and thus there can be no snappage)
		if len(POT) == 1:
			continue

		# Check if the top two cards in the pot snap
		isSnap = RULES.isSnap(POT[-1], POT[-2])

		# Have each player do their move
		[player.doMove(isSnap) for player in PLAYERS]

		if isSnap:
			processSnap()
		else:
			processNoSnap()

	announceWinner()

def processSnap():
	"""
	Finds the winner and pays out the pot.
	"""
	# Find the player that snapped the fastest
	# TODO: Handle draws
	winningPlayer = min(PLAYERS, key = lambda player: player.snapResponseTime)

	if winningPlayer.name == "Hulk":
		print "HULK SNAP!!!"
	else:
		print "%s won the snap!" % winningPlayer

	# Hand out the pot
	winningPlayer.addCards(POT)
	del POT[:]

def processNoSnap():
	"""
	Checks if any players mis-snapped and penalizes them.
	"""
	for player in PLAYERS:
		if player.snapResponseTime > 0:
			print "%s mis-snapped and took a 2 card penalty!" % player
			player.removeCards(2)

def announceWinner():
	"""
	Finds and announces the winner and asks if a rematch is desired.
	"""
	winningPlayer = max(PLAYERS, key = lambda player: player.getCardCount())
	print "\n%s won the game with %i cards!\n" % (winningPlayer, winningPlayer.getCardCount())
	checkRematch()

def checkRematch():
	"""
	Checks if a rematch should be performed and begins it if so.
	"""
	if _getRematchResponse():
		# Reset the hands of each player
		for player in PLAYERS:
			player.resetHand()

		# Empty the pot
		del POT[:]

		# Start the new game
		start(NUMBER_OF_PACKS, PLAYERS, RULES)

def _getRematchResponse():
	"""
	Asks the user if they would like a rematch.

	:return:
		True if yes, false otherwise.
	"""
	try:
		replay = raw_input("Would you like a rematch (y/n)? ")
		if replay == "y" or replay == "yes" or replay == "1":
			return True
		elif replay == "n" or replay == "no" or replay == "0":
			return False
		raise ValueError("Invalid response.")
	except ValueError:
		print "Please enter yes or no"
		return _getRematchResponse()
