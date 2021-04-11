import json
import sadface as sf
import fileManager as fm
import translation as t
from zipfile import ZipFile
import os
from os.path import basename

zipObj = ZipFile('arguments.zip', 'w')
#get list of file names
fileList = os.listdir("arguments")
#loop through list and add all to .zip
for file in fileList:
    zipObj.write("arguments/"+file)

zipObj.close()


'''
def createArgArr():
    #will add arguments to the file created in test_addPrompt()
    prompt = "test prompt"
    newArgument = "test argument"
    parent = "test prompt"
    stance = "agree"
    argArr = [prompt, newArgument, parent, stance]
    return argArr

argArr = createArgArr()
prompt = argArr[0]
t.addPrompt(prompt)

fm.deleteFile("test argument")


sfStr = fm.getFile("test argument.json")
arguments = t.getArguments(sfStr)
print(arguments)


sf.config.init("SADFace/test.cfg")
sf.initialise()

sf.set_title("test argument")


#simple argument for testing

#set base statement
statement = "test argument"
sf.add_atom(statement)
sf.set_claim(sf.get_atom_id("test argument"))
#set supporting point
support = ["level one agree"]
sf.add_support(None, support, sf.get_atom_id("test argument"), None)

#opposing point
oppose = "level one disagree"
sf.add_conflict(None, oppose, sf.get_atom_id("test argument"), None)


#dot = sf.export_dot()#trad=False)    # Uncomment to use the brewer colourscheme
#with open('out.dot', 'w') as file:
    #file.write(dot)
#sf.save("saves", "json")


sfJSON = sf.export_json()
fm.createFile(sfJSON)
'''