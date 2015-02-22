import service.card_service as cardService

class Game(object):
	def __init__(self, numberOfPacks, players, rules):
		"""
		Initializes the game and begins the match.

		:param numberOfPacks:
			The number of packs to use.
		:param players:
			The players.
		:param rules:
			The game rules.
		"""
		self.numberOfPacks = numberOfPacks
		self.deck = cardService.getDeck(numberOfPacks)
		self.players = players
		self.rules = rules

		# The pot holds the current cards that have been played
		self.pot = []

		print "\n%s\n" % '\nvs\n'.join([player.__str__() for player in players])

	def run(self):
		self._run(self.announceWinner)

	def _run(self, gameFinishedMethod):
		"""
		The main game loop that plays out each round.
		"""
		# Keep going until there's no deck left
		while len(self.deck) > 0:
			card = self.deck.pop()
			print "The dealer turned the %s" % card
			self.pot.append(card)

			# Skip this round if this is the first card in the current pot (and thus there can be no snappage)
			if len(self.pot) == 1:
				continue

			# Check if the top two cards in the pot snap
			isSnap = self.rules.isSnap(self.pot[-1], self.pot[-2])

			# Have each player do their move
			[player.doMove(isSnap) for player in self.players]

			if isSnap:
				self.processSnap()
			else:
				self.processNoSnap()

		gameFinishedMethod()

	def processSnap(self):
		"""
		Finds the winner and pays out the pot.
		"""
		# Find the player that snapped the fastest
		# TODO: Handle draws
		winningPlayer = min(self.players, key = lambda player: player.snapResponseTime)

		if winningPlayer.name == "Hulk":
			print "HULK SNAP!!!"
		else:
			print "%s won the snap!" % winningPlayer.name

		# Hand out the pot
		winningPlayer.addCards(self.pot)
		del self.pot[:]

	def processNoSnap(self):
		"""
		Checks if any players mis-snapped and penalizes them.
		"""
		for player in self.players:
			if player.snapResponseTime > 0:
				print "%s mis-snapped and took a 2 card penalty!" % player.name
				player.removeCards(2)

	def announceWinner(self):
		self._announceWinner(self.checkRematch)

	def _announceWinner(self, checkRematchMethod):
		"""
		Finds and announces the winner and asks if a rematch is desired.
		"""
		winningPlayer = max(self.players, key = lambda player: player.getCardCount())

		# Find any other players that may have drawn
		winningPlayers = [player for player in self.players if player.getCardCount() == winningPlayer.getCardCount()]

		if len(winningPlayers) == 1:
			print "\n%s won the game with %i cards!\n" % (winningPlayers[0].name, winningPlayers[0].getCardCount())
		else:
			print "\n%s drew the game with %i cards each!\n" % \
				  (' & '.join([winningPlayer.name for winningPlayer in winningPlayers]), winningPlayers[0].getCardCount())

		checkRematchMethod()

	def checkRematch(self):
		self._checkRematch(self._getRematchResponse, self.run)

	def _checkRematch(self, getRematchResponseMethod, runMethod):
		"""
		Checks if a rematch should be performed and begins it if so.
		"""
		if getRematchResponseMethod():
			# Reset the hands of each player
			for player in self.players:
				player.resetHand()

			# Reinitialise the game
			self.__init__(self.numberOfPacks, self.players, self.rules)
			runMethod()

	def _getRematchResponse(self):
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
			return self._getRematchResponse()
