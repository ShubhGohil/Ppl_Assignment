#abstraction and encapsulation
from abc import ABC,abstractmethod
class Animal(ABC):
	def type(self):
		print('I am an animal')
	def speak(self):
		print('I can\'t speak')
class Dog(Animal):
	def  __init__(self):
		self.__legs = 4
		self.__breed = 'pug'
		self.__colour = 'white'
		breead = 's'
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
	def personality(self):
		super().type()
	def speak(self):
		super().speak()
	
class Pug(Dog,Animal):
	def type(self):
		print('I am a breed of dog')
	def color(self):
		Dog.display_colour(self)

class Cat(Animal):
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
	def personality(self):
		super().type()
	def speak(self):
		super().speak()



class Fish(Animal):
	def  __init__(self):
		self.__life_span = 4
		self.__species = 'gold fish'
		self.__colour = 'white'
	def set_life_span(self,life):
		self.__life_span = life_span
	def display_life_span(self):
		print(self.__legs + 'yrs')
	def set_breed(self,species):
		self.__species = species
	def display_breed(self):
		print(self.__breed)
	def set_colour(self,colour):
		self.__colour = colour
	def display_colour(self):
		print(self.__colour)
	def personality(self):
		super().type()
	def speak(self):
		super().speak()



class parrot(Animal):
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
	def personality(self):
		super().type()
	def speak(self):
		super().speak()


class Human():
	def speak(self):
		print('I can talk')
	def move(self):
		print('I can walk')
		

