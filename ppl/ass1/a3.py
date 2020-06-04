import time
from datetime import datetime as dt

host = "/etc/hosts"
number = int(input("Enter the number of sites to be blocked:"))
website_list = []
for i in range(0,number):
	website = input("Enter the name of the host site:")
	website_list.append(website)

#starttime = int(input("Enter the start time in 24 hr format:"))
#endtime = int(input("Enter the end time in 24 hr format:"))
redirect = "127.0.0.2"

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day,17) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18): 
		f = open(host, 'rt')
		content = f.read()
		for wesite in website_list:
			if website in content:
				pass
			else:
				f.write(redirect+" "+website)
	else:
		f = open(host, 'r+')
		lines = f.readlines()
		if not any(website in lines for website in website_list):
			f.write(lines)
		f.truncate()
	time.sleep(10)
