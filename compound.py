from rastav import *


##############################################################


class Compound():
	def __init__(self, name, line_length=50):
		if not name or not line_length:
			return

		self.name = name
		self.line_length = line_length
		self.number_of_atoms, self.substituents_list, self.is_cyclic = prevedi(self.name)