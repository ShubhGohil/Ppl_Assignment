import os
fh = open('test.txt','w')
fh.write('This is just a demonstration of file handling')
fh.close()
os.remove('test.txt')
try:
	fh = open('test.txt','r')
except FileNotFoundError:
	print('No such file exists')

