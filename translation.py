import sadface as sf
import json
import fileManager as fm
#these methods translate from the json encoded strings that datastore.py deals with to the variables needed in server.py

#gets the debates prompt
def getPrompt(sfStr):
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)
    claim = sf.get_claim()
    prompt = sf.get_atom_text(claim)
    return prompt

#get random argument
#no arguments
#returns array with title, pro argument, con argument
def getArguments(sfStr):
    #set sf document
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)

    #get connections to the claim
    connections = sf.get_connections(sf.get_claim())
    #print(connections)

    #get arguments
    arglist = sf.list_arguments()
    #print(arglist)
 
    #get target ids
    #find the target ids that appear twice
    #use these target ids to get assosicated source ids in all edges
    #use the target id from that source id to get the text for the argument/weather its pro or con

    #get duplicate target ids
    targetIDs = []
    for edge in connections:
        #print(edge["target_id"])
        targetIDs.append(edge["target_id"])
    
    duplicateTIDs = []
    for i in range(0, len(targetIDs)):
        for j in range(0, len(targetIDs)):
            if(targetIDs[i] == targetIDs[j]):
                duplicateTIDs.append(targetIDs[i])
                
    #removes duplicate entries, leaving only one copy of every target_id that shows up in 'connections' more than once
    duplicateTIDs = list(set(duplicateTIDs)) 

    #for i in range(0, (len(duplicateTIDs))):
    #    print("t_id : " + str(duplicateTIDs[i]))

    #find corresponding souce_ids 
    #get edges
    edges = sfJSON["edges"]
    sourceIDs = []
    for edge in edges:
        if edge["target_id"] in duplicateTIDs:
            sourceIDs.append(edge["source_id"])

    #get corresponding target_id to those source ids
    argIDs = []
    for edge in edges:
        if edge["target_id"] in sourceIDs:
            argIDs.append(edge["source_id"])

    #print(argIDs)
    #get atom text for that target_id
    #make list to return
    arguments = []
    for i in range(0, len(argIDs)):
        arguments.append(sf.get_atom_text(argIDs[i]))

    return arguments


#add argument
#argument = array with title, parent argument, pro/con, text
#returns status
def addArgument(argArr):
    #split argument array into parts
    prompt = argArr[0]
    newArgument = argArr[1]
    parent = argArr[2]
    stance = argArr[3]

    print(argArr[1])
    
    #get sf doc
    sfStr = fm.getFile(prompt+".json")
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)

    #create argument
    if(stance == "agree"):
        sf.add_support(None, [newArgument], sf.get_atom_id(parent), None)
    else:
        sf.add_conflict(None, newArgument, sf.get_atom_id(parent), None)
    
    #write updated sfDoc to file
    sfJSONex = sf.export_json()
    fm.createFile(sfJSONex)

    return None

#add prompt
#argument = prompt
#returns status
def addPrompt(prompt):
    #set metadata
    #create sf doc
    sf.initialise()
    #add prompt statement
    sf.add_atom(prompt)
    #set prompt as claim
    sf.set_claim(sf.get_atom_id(prompt))
    #set title
    sf.set_title(prompt)

    #create file
    sfJSON = sf.export_json()
    fm.createFile(sfJSON)

    return None

#add vote
#argument = array with title and argument voted for
#returns status