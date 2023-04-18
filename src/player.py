# Class to represent player.
class Player:

	def __init__(self, rep, ref):
		# Number reference to determine winner.
		self._ref = ref
		# String representation of player.
		self._rep = rep

	def get_ref(self):
		return self._ref

	def get_rep(self):
		return self._rep

	def __repr__(self):
		return self.get_rep()

	def __str__(self):
		return self.get_rep()