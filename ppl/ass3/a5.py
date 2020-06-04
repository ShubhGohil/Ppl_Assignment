class parrot():
	def  __init__(self):
		self.__legs = 2
		self.__species = 'red neck parraket'
		self.__colour = 'white'
	def set_legs(self,leg):
		self.__legs = leg
	def display_legs(self):
		print(self.__legs)
	def set_species(self,specie):
		self.__species = specie
	def display_species(self):
		print(self.__species)
	def set_colour(self,colour):
		self.__colour = colour
	def display_colour(self):
		print(self.__colour)

