class Dog():
	def  __init__(self):
		self.__legs = 4
		self.__breed = 'pug'
		self.__colour = 'white'
		breed = 's'
	def set_legs(self,leg):
		self.__legs = leg
	def display_legs(self):
		print(self.__legs)
	def set_breed(self,breed):
		self.__breed = breed
	def display_breed(self):
		print(self.__breed)
	def set_colour(self,colour):
		self.__colour = colour
	def display_colour(self):
		print(self.__colour)

	def __str__(self):
		return "I am a dog"
	def __repr__(self):
		return "I am an object of Class Dog()"

