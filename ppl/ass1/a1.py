def check(option,bank) :
	if bank == '1':
		if option in bank1:
			return True
		else:
			return False
	elif bank == '2':
		if option in bank2:
			return True
		else:
			return False
	else:
		return False

def verifymove(bank,check1,check2):
	if bank == '1':
		if set(check1).issubset(set(bank1)): 
			return True
		elif set(check2).issubset(set(bank1)):
			return True
		else:
			return False
	elif bank == '2':
		if set(check1).issubset(set(bank2)):
			return True
		elif set(check2).issubset(set(bank2)):
			return True
		else:
			return False
	
person = input("Enter the name of person:")
wanimal = input("Enter the name of wild animal:")
danimal = input("Enter the name of domestic animal:")
food = input("Enter the food:")
print("Enter 'n' if you want to cross river with empty boat")
bank1,bank2,boat = [],[],[]
bank1.extend([wanimal,danimal,food])
check1 = [wanimal,danimal]
check2 = [danimal,food]
boat.append(person)
print(bank1,"-----",boat,"-----",bank2)
bank2.append("n")
while len(bank1)!= 0:
	option,bank = input("Who is to be sent on the other side and from which bank:").split()
	value = check(option,bank)
	if value == True:
		if bank == '1':
			if option != 'n':
				bank1.remove(option)
			if verifymove(bank,check1,check2):
				break
			boat.append(option)
			boat.remove(option)
			if option != 'n':
				bank2.append(option)
		elif bank == '2':
			if option != 'n':
				bank2.remove(option)
			if verifymove(bank,check1,check2):
				break
			boat.append(option)
			boat.remove(option)
			if option != 'n':	
				bank1.append(option)
	else:
		print("Wrong answer.Try again")
		break
if len(bank1)!= 0:
	bank2.remove("n")
	print(bank1,'-----',boat,'-----',bank2)
