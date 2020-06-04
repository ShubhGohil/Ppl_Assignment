class Circle():
	def  __init__(self):
		self.__radius = 1
		self.__xcoordofcenter = 0
		self.__ycoordofcenter = 0
	def set_radius(self,r):
		self.__radius = r
	def set_xcoordofcenter(self,x):
		self.__xcoordofcenter = x
	def set_ycoordofcenter(self,y):
		self.__ycoordofcenter = y
	def display_area(self):
		return 4*3.14*(self.__radius**2)
	def display_perimeter(self):
		return 2*3.14*(self.__radius)
	def display_center(self):
		return (self.__xcoordofcenter,self.__ycoordofcenter)

