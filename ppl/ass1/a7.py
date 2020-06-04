urange, lrange = map(int, input().split())
for temp in range(urange, lrange+1) :
	length = len(str(temp))
	add = 0
	num = temp
	while temp > 0 : 
		add += (temp%10)**length
		temp = temp//10
	if add == num :
		print (add)
