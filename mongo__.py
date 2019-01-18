from pymongo import MongoClient

MongoHost = "mongodb://localhost:27017"
client = MongoClient(MongoHost)
MongoDB_ = client.HIBP
Collection_ = "Data"#. So client.HIBP.Data
# Change collection to BreachData

emailDB = client.HIBP_Emails
emailDB_Collection = "Emails"


def queryExistingUsers(email):
    userQuery = emailDB.emailDB_Collection.find_one({'email': email})
    if str(userQuery) == "None":
        return True
    else:
        return False
    
def displayAllEmails():
    resultList = []
    result = emailDB.emailDB_Collection.distinct('email')
    for email in result['email']:
        resultList.append(email)
    return resultList

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

def checkExistingBreachRecords(email, breach):
    try:
        MongoDB_.Collection_.find_one({'email': email, 'breach': breach})
        return True
    except Exception as e:
        print(e)
        return False

def insertMongo(email, breach, domain, verified, dataType):
           

    print("hg")



    