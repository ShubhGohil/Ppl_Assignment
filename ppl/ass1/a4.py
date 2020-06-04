import random as ran
key = ran.randint(1,100)
for i in range(1,4) :
	num = int(input())
	if num == key :
		print("Number found\n")
	elif num > key :
		print("Number is less than your guess\n")
		if i == 3 :
			print("Try again\n")
	elif num < key :
		print("Number is greater than your guess\n")
		if i == 3 :
			print("Try again\n")
	
