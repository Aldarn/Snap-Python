from domain.card_types import VALUES, SUITS

class Card(object):
	def __init__(self, value, suit):
		self._value = value
		self._suit = suit

	@property
	def value(self):
		return self._value

	@property
	def suit(self):
		return self._suit

	def __str__(self):
		return "%s of %s" % (VALUES.get(self.value), SUITS.get(self.suit))

	def __repr__(self):
		return "Card(%s, %s)" % (self.value, self.suit)
