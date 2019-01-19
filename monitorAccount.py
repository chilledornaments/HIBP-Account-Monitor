#!/usr/bin/env python36
import requests, json, sys
from time import sleep
import mongo__

def QueryAPI():

    headers = {
        'User-Agent': 'BHI HIBP Account Monitoring'
    }
    emailList = mongo__.displayAllEmails()
    for email in emailList:
        print("Checking {}".format(email))
        URL = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" %(email)
        sleep(5)
        r = requests.get(URL, headers=headers)
        print("Checked against HIBP")


        if r.status_code == 404:
            # There isn't a breach associated with this email
            print("No breaches found")
            pass
        elif r.status_code == 429:
            print("Making too many requests. Waiting 30 seconds")
            sleep(30)
        
        else:
            jsonLoaded = json.loads(r.text)
            for breach in jsonLoaded:
                
                breachName = breach['Name']
                domain = breach['Domain']
                verified = breach['IsVerified']
                dataType = breach['DataClasses']
                insertResult = mongo__.insertMongo(email, breachName, domain, verified, dataType)
                print(insertResult)


if __name__ == '__main__':
        QueryAPI()