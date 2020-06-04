import math
class Rectangle():
	def  __init__(self):
		self.__length = 1
		self.__breadth = 1
	def set_length(self,l):
		self.__length = l
	def set_breadth(self,b):
		self.__breadth = b
	def display_area(self):
		return self.__length*self.__breadth
	def display_perimeter(self):
		return 2*(self.__length+self.__breadth)
	def display_lenofdia(self):
		return math.sqrt((self.__length**2)+(self.__breadth**2))

