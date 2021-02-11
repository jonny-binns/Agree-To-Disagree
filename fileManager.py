import sadface as sf
import os
import random
import json
#these methods control all of the reading/writing from/to the individual json files that store each argument 

#get random file
def getRandomFile():
    #get list of file names
    fileList = os.listdir("arguments")

    #pick random number between 0 and no of files
    randno = random.randint(0,(len(fileList)-1))

    #read from corresponding file
    f = open("arguments/"+fileList[randno], "r")
    fStr = f.read()
    return fStr

#gets a specific file based on its title
def getFile(title):
    #get list of file names
    fileList = os.listdir("arguments")

    #loop through file list and store file name when name=title
    fileName = None
    for x in range(len(fileList)):
        if(fileList[x] == title):
            fileName = fileList[x]


    #read from corresponding file
    f = open("arguments/"+fileName, "r")
    fStr = f.read()
    return fStr

#make new file
#Also used for updating files with new arguments 
def createFile(sfStr):
    #convert string to json then set sadface doc
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)
    
    #get title then save as title.json
    title = sf.get_title()
    sf.save("arguments/"+title, "json")

    #update to return error code
    return None