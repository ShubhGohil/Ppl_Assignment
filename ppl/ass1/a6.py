numbers = {}
result = []

def calculatedivisor(num):
	sum = 0
	for i in range(1,num):
		if num%i==0:
			sum += i
	return sum		
i,count = 0,10
while count:
	i = i + 1
	value=[]
	numbers[i] = calculatedivisor(i)
	try:
		num2 = numbers[numbers[i]]
		if (num2 == i) and (i!=numbers[i]):
			value = [i,numbers[i]]
			result.append(value)
			count-=1 
	except KeyError:
		pass	
print(result)

