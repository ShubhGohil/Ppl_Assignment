#polymorphism and hierarchy
import math
from abc import ABC
class ShapeC(ABC):
	def area_of_sphere(self,r):
		return 4*3.14*(r**3)
	def area_of_circle(self,r):
		return 4*3.14*(r**2)
	def perimeter_of_circle(self,r):
		return 2*3.14*(r)

class ShapeS():
	def area_of_square(self,s):
		return s**2
	def area_of_rectangle(self,l,b):
		return l*b
	def perimeter_of_rectangle(self,r):
		return 2*(l+b)


class Sphere(ShapeC):
	def  __init__(self):
		self.__radius = 1
	def set_radius(self,r):
		self.__radius = r
	def display_area(self):
		return ShapeC.area_of_sphere(self,self.__radius)

class Circle(ShapeC):
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
		return ShapeC.area_of_circle(self,self.__radius)
	def display_perimeter(self):
		return ShapeC.perimeter_of_circle(self.__radius)
	def display_center(self):
		return (self.__xcoordofcenter,self.__ycoordofcenter)
class Square(ShapeS):
	def  __init__(self):
		self.__side = 1
	def set_side(self,typ):
		self.__side = side
	def display_area(self):
		return ShapeS.area_of_square(self,self.__side)
	def display_perimeter(self):
		return 4*(self.__radius)
	def display_center(self):
		return (self.__xcoordofcenter,self.__ycoordofcenter)
	def display_lenofdia(self):
		return 1.414*self.__side

class Rectangle(ShapeS):
	def  __init__(self):
		self.__length = 1
		self.__breadth = 1
	def set_length(self,l):
		self.__length = l
	def set_breadth(self,b):
		self.__breadth = b
	def display_area(self):
		return ShapeS.area_of_rectangle(self,self.__length,self.__breadth)
	def display_perimeter(self):
		return ShapeS.perimeter_of_rectangle(self,self.__length,self.__breadth)
	def display_lenofdia(self):
		return math.sqrt((self.__length**2)+(self.__breadth**2))

class Triangle():
	def  __init__(self):
		self.__s1 = 1
		self.__s2 = 1
		self.__s3 = 1
	def set_sides(self,s1,s2,s3):
		self.__s1 = s1
		self.__s2 = s2
		self.__s3 = s3
	def display_area(self):
		s = (self.__s1+self.__s2+self.__s3)/3
		return math.sqrt(s*(s-self.__s1)*(s-self.__s2)*(s-self.__s3))
	def display_perimeter(self):
		return self.__s1+self.__s2+self.__s3


