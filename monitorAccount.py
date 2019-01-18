#!/usr/bin/env python36
import requests, json, sys
from time import sleep
import mongo__
from mongo__ import MongoDB_


def QueryAPI():

    headers = {
        'User-Agent': 'BHI HIBP Account Monitoring'
    }
    emailList = mongo__.displayAllEmails()
    for email in emailList:
        URL = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" %(email)
        sleep(5)
        r = requests.get(URL, headers=headers)


        if r.status_code == 404:
            pass
        elif r.status_code == 429:
            print("Making too many requests. Waiting 30 seconds")
            sleep(30)
        
        else:
            print(email)
            jsonLoaded = json.loads(r.text)
            for breach in jsonLoaded:
                
                breachName = breach['Name']
                print(breachName)


if __name__ == '__main__':
        QueryAPI()