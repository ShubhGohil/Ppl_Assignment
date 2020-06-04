
numbers = list(map(int, input().split(' ')))
nnumbers = []
if numbers[0] > 2 :
	a = numbers[0] - 2
	while a > 0 :
		nnumbers.append(a)
		a -= 2
for a in range(1,len(numbers)) :
	diff = numbers[a] - numbers[a-1]
	if diff > 2 :
		for temp in range(2,diff,2) :
			nnumbers.append(numbers[a-1]+temp) 
print(nnumbers)			

