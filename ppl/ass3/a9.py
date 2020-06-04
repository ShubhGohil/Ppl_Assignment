import math
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

