class Cat():
	def  __init__(self):
		self.__legs = 4
		self.__species = 'ragdoll'
		self.__colour = 'brown with black strips'
	def set_legs(self,leg):
		self.__legs = leg
	def display_legs(self):
		print(self.__legs)
	def set_species(self,specie):
		self.__species = specie
	def display_species(self):
		print(self.__breed)
	def set_colour(self,colour):
		self.__colour = colour
	def display_colour(self):
		print(self.__colour)

