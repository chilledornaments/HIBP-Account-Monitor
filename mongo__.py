from pymongo import MongoClient

MongoHost = "mongodb://localhost:27017"
client = MongoClient(MongoHost)
BreachInfoDB = client.HIBP
BreachInfoCollection = "Data"#. So client.HIBP.Data
# Change collection to BreachData

emailDB = client.HIBP_Emails
emailDB_Collection = "Emails"

# queryExistingUsers function is used by newUserRecord
# To check if an email already exists in the database
def queryExistingUsers(email):
    userQuery = emailDB.emailDB_Collection.find_one({'email': email})
    if str(userQuery) == "None":
        return True
    else:
        return False
    
# displayAllEmails is used by monitorAccount.py to check which emails to search for
def displayAllEmails():
    resultList = []
    result = emailDB.emailDB_Collection.distinct('email')
    for email in result['email']:
        resultList.append(email)
    return resultList

# newUserRecord is used by initialMongoImport.py to add emails to emailDB
def newUserRecord(email):
    queryResult = queryExistingUsers(email)

    if queryResult:
    
        try:
            emailDB.emailDB_Collection.insert_one({'email': email})
            return "Email {} added to {}.{}".format(email, emailDB, emailDB_Collection)
        except Exception as err:
            return "Error adding {} to database.\nError: {}".format(email, str(err))
    else:
        return "Record {} already exists".format(email)

# checkExistingBreachRecords is used by insertMongo to see if a breach has already been added
# This avoids duplicating data
def checkExistingBreachRecords(email, breach):
    try:
        existingBreachCheck = BreachInfoDB.BreachInfoCollection.find_one({'email': email, 'breach': breach})
        if existingBreachCheck != "None":
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# insertMongo is the heart of monitorAccount.py 
# It checks for an existing email:breach record to avoid duplicates
# If there won't be a duplicate, the record is added to the collection
def insertMongo(email, breach, domain, verified, dataType):
    queryResult = checkExistingBreachRecords(email, breach)
    if queryResult:
        return "{} Already has a record for {}. Not adding to database".format(email, breach)
    else:
        try:
            BreachInfoDB.BreachInfoCollection.insert_one({'email': email, 'breach': breach, 'domain': domain, 'verified': verified, 'dataType': dataType})
            return "Success"
        except Exception as e:
            return str(e)




    