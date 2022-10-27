import pymongo
from bson.objectid import ObjectId

# Connecting to mongo client
client = pymongo.MongoClient("mongodb+srv://PaperPlane:PaperPlane@cluster0.dqen3xq.mongodb.net/?retryWrites=true&w=majority")
myDatabase = client.MOVIES
variables = myDatabase.variables
userRequests = myDatabase.userRequests
noFilesFound = myDatabase.noFilesFound
botsNotWorking = myDatabase.botsNotWorking
upcomingMovies = myDatabase.upcomingMovies
uploadedMovies = myDatabase.uploadedMovies
exceptException = myDatabase.exceptException
titleNotDefined = myDatabase.titleNotDefined

#This function is to add movies in upcoming list, if more then 1 movies seperate them by +
def addMovieToUpcomingList(rawData):
    try:
        data, count = [], 0
        mata = [x for x in upcomingMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        sata = [x for x in uploadedMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        if "|" in rawData:
            finalData = rawData.split("|")
            for x in finalData:
                halo = {"movieName": x[:len(x)-5].lower(), "releaseYear": x[-4:]}
                if halo not in sata:
                    if halo not in mata:
                        data.append(halo)
                        count += 1
            upcomingMovies.insert_many(data)
        else:
            kalo = {"movieName": rawData[:len(rawData)-5].lower(), "releaseYear": rawData[-4:]}
            if kalo in sata:
                return count
            if kalo not in mata:
                upcomingMovies.insert_one(kalo)
                count += 1
        return count
    except TypeError:
        return count

# This function is to get the movie from list and delete that also
def giveMovie():
    mode = list(variables.find({}, {"_id": 0, "maintenanceMode": 1}))[0]["maintenanceMode"]
    if mode == "on":
        return "Permission Denied", ""
    try:
        movie = list(upcomingMovies.find({}, {"_id": 0, "movieName": 1, "releaseYear": 1}))[0]
        upcomingMovies.delete_one(movie)
        return movie["movieName"].title(), movie["releaseYear"]
    except IndexError:
        return "No movies left in upcomingList.", ""
    
def petrionaMessageId(messageId):
    if len(list(variables.find({}, {"_id":0, "petrionaMessageId": 1}))) == 0:
        variables.insert_one({"petrionaMessageId": messageId})
    old = list(variables.find({}, {"_id":0, "petrionaMessageId": 1}))[0]
    new = {"$set": {"petrionaMessageId": messageId}}
    variables.update_one(old, new)
    return
    
def maintenanceMode(mode):
    if len(list(variables.find({}, {"_id": 0, "maintenanceMode": 1}))) == 0:
        variables.insert_one({"maintenanceMode": "off"})
    old = list(variables.find({}, {"_id": 0, "maintenanceMode": 1}))[0]
    new = {"$set": {"maintenanceMode": mode}}
    variables.update_one(old, new)
    return
   
def petrionaUploading(movie, nums):
    if len([x for x in variables.find({}, {"_id":0, "petrionaUploading": 1, "files": 1})]) == 0:
        variables.insert_one({"petrionaUploading": 1, "files": 1})
    old = variables.find({}, {"_id":0, "petrionaUploading": 1, "files": 1})[0]
    new = {"$set": {"petrionaUploading": movie, "files": nums }}
    variables.update_one(old, new)
    return

def fastUpload(query):
    oldData = [x for x in upcomingMovies.find({}, {"_id": 0, "movieName": 1, "releaseYear": 1})]
    upcomingMovies.drop()
    upcomingMovies.insert_one({"movieName": query[:len(query)-5].lower(), "releaseYear": query[-4:]})
    try:
        upcomingMovies.insert_many(oldData)
    except TypeError:
        pass
    return

def shift(query):
    upcomingMovies.delete_one({"movieName": query[:len(query)-5].lower(), "releaseYear": query[-4:]})
    oldData = [x for x in upcomingMovies.find({}, {"_id": 0, "movieName": 1, "releaseYear": 1})]
    upcomingMovies.drop()
    upcomingMovies.insert_one({"movieName": query[:len(query)-5].lower(), "releaseYear": query[-4:]})
    try:
        upcomingMovies.insert_many(oldData)
    except TypeError:
        pass
    return

def updateStatusMessageId(Id):
    if len([x for x in variables.find({}, {"_id":0, "statusMessageId": 1})]) == 0:
        variables.insert_one({"_id": 0, "statusMessageId": 0})
    old = variables.find({}, {"_id": 0, "statusMessageId": 1})[0]
    new = {"$set": {"statusMessageId": Id}}
    variables.update_one(old, new)
    
def searchStatusMessageId():
    if len([x for x in variables.find({}, {"_id":0, "statusMessageId": 1})]) == 0:
        variables.insert_one({"_id": 0, "statusMessageId": 0})
    Id = variables.find({}, {"_id": 0, "statusMessageId": 1})[0]['statusMessageId']
    return Id

def removeMovieFromUpcomingList(query):
    upcomingMovies.delete_one({"movieName": query[:len(query)-5].lower(), "releaseYear": query[-4:]})
    return

def removeMovieFromUploadedMovies(Id):
    uploadedMovies.delete_one({'_id': ObjectId(Id)}) 
    return
  
def addInUploadedMovies(movie, year, links):
    uploadedMovies.insert_one({"movieName": movie.lower(), "releaseYear": year, "links": links})

def addInUserRequests(data):
    userRequests.insert_one({"movie": data})
    
    # Errors
    
def addInNoFilesFound(movie, year):
    noFilesFound.insert_one({"movieName": movie.lower(), "releaseYear": year})
      
def addInBotsNotWorking(movie, year):
    if len(list(botsNotWorking.find())) == 3:
        return setPermission("false")
    botsNotWorking.insert_one({"movieName": movie.lower(), "releaseYear": year})

def addInExceptException(movie, year):
    if len(list(exceptException.find())) == 3:
        return setPermission("false")
    exceptException.insert_one({"movieName": movie.lower(), "releaseYear": year})
    
def addInTitleNotDefined(movie, year):
    if len(list(titleNotDefined.find())) == 3:
        return setPermission("false")
    titleNotDefined.insert_one({"movieName": movie.lower(), "releaseYear": year})

# I wrote this to check if addMovieToUpcomingList() function is working or not?
# ask = input("Enter Movie Name you want to upload: ")
# hala = addMovieToUpcomingList(ask)
# if hala != 0:
#     print(f"Successfully added {hala} movies in upcomingList.")
# else:
#     print("I did not added any movie to upcomingMovie because all movies are alreayd in list.")

# I wrote this to check if deleteOneMovieFromUpcominglist() function is working or not?
# print(deleteOneMovieFromUpcominglist()) 
