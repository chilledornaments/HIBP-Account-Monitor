#!/usr/bin/env python3
import requests, json, sys
from time import sleep
import mongo__

"""

Used for loading email address into Mongo.HIBP_Emails.Emails

Script takes new line delimited file as argument
"""

emailList = []

emailListFile = sys.argv[1]
with open(emailListFile, "r") as F:
    for line in F.read().splitlines():
        print(mongo__.newUserRecord(line))

