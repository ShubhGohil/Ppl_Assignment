class Sphere():
	def  __init__(self):
		self.__radius = 1
	def set_radius(self,r):
		self.__radius = r
	def display_area(self):
		return 4*3.14*(self.__radius**3)

