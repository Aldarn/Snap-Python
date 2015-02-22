class Card(object):
	SUITS = {
		"h": "Hearts",
		"d": "Diamonds",
		"c": "Clubs",
		"s": "Spades"
	}

	VALUES = {
		"a": "Ace",
		"2": "Two",
		"3": "Three",
		"4": "Four",
		"5": "Five",
		"6": "Six",
		"7": "Seven",
		"8": "Eight",
		"9": "Nine",
		"t": "Ten",
		"j": "Jack",
		"q": "Queen",
		"k": "King"
	}

	def __init__(self, cardString):
		self._value = cardString[0]
		self._suit = cardString[1]

	@property
	def value(self):
		return self._value

	@property
	def suit(self):
		return self._suit

	def __str__(self):
		return "%s of %s" % (Card.VALUES.get(self.value), Card.SUITS.get(self.suit))

	def __repr__(self):
		return "Card(%s, %s)" % (self.value, self.suit)
