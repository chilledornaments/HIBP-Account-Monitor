#!/usr/bin/env python3
import requests, json, hashlib
from sys import argv
# Tool to check PW hashes against Pwned Passwords

PW = argv[1]
PW = PW.encode('utf-8')

PWHASH = hashlib.sha1(PW).hexdigest().upper()
PwndedHashPrefix = PWHASH[0:5]
PwndedHashSuffix = PWHASH[5:]


print("Using PW Hash: {}".format(PwndedHashPrefix))

HEADERS = {'User-Agent': 'BHI Pwned PW Checker'}

r = requests.get("https://api.pwnedpasswords.com/range/"+PwndedHashPrefix, headers=HEADERS)

if r.status_code == 200:
    print("Success Searching Pwned Passwords Database")
else:
    print("Error Searching Pwned Passwords Database")

for line in r.text.splitlines():
    hashSuffix, count = line.split(':')

    if hashSuffix == PwndedHashSuffix:
        print("Your password has been breached {} times".format(str(count)))



