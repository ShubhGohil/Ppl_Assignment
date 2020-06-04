a,b,c,d = [int(i) for i in input().split()]
try:
	sum = a+(b*c)/d
except ZeroDivisionError:
	print('The value of d cannot be 0')
