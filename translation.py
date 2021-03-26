import sadface as sf
import json
import fileManager as fm
import random
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
    #set SF doc
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)

    #get atoms
    atomlist = sf.list_atoms()

    #pick random atom
    randInt = random.randint(0, len(atomlist)-1)
    randArgID = atomlist[randInt]["id"]
    currentArgument = atomlist[randInt]["text"]

    #get children/connections of that argument
    connections = sf.get_connections(randArgID)

    #loop through connections and if target_id = randArgID add the source_id in the list
    #get the edges connecting the argument to its children
    childConnection = []
    for connection in connections:
        if(connection["target_id"] == randArgID):
            childConnection.append(connection["source_id"])

    #get the atoms that are at the end of these edges
    #loop through edges to find the source_id when the target_id is contained in childrenEdge
    childrenEdgeID = []
    edges = sfJSON["edges"]
    for edge in edges: 
        for i in range(0, len(childConnection)):
            if(edge["target_id"] == childConnection[i]):
                childrenEdgeID.append(edge["id"])


    #for each edge in childrenEdgeID, source_id = atom with arg text, target_id = weather arg is support or conflict
    arguments = []
    proArgument = None
    conArgument = None

    #loop through edge in childrenEdgeID
    for i in range(0, len(childrenEdgeID)):
        edge = sf.get_edge(childrenEdgeID[i])
        target = sf.get_atom(edge["target_id"])
        stance = target["name"]
        #check whether arg is support or conflict then set text to relevent variable
        if(stance == "support"):
            proArgument = sf.get_atom_text(edge["source_id"])
        if(stance == "conflict"):
            conArgument = sf.get_atom_text(edge["source_id"])
        

    #check that both pro/con argument are populated, if not populate with generic sentence
    if(proArgument == None):
        proArgument = "Looks like there is no supporting argument, to add one respond directly to the argument and click agree"
    if(conArgument == None):
        conArgument = "Looks like there is no opposing argument, to add one respond directly to the argument and click disagree"

    arguments.append(currentArgument)
    arguments.append(proArgument)
    arguments.append(conArgument)
    return arguments


def getData(sfStr):
    #set SF doc
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)

    #create return array
    #key for return array [parent text][atom text][atom stance]
    cols = 3
    rows = len(sf.list_atoms())
    #initialises all elements to 'a'
    data = [["a" for i in range(cols)]for j in range(rows)]
    

    #populate return array
    #print(sf.list_atoms())

    #add debate prompt as edge case
    data[0][0] = "null"
    data[0][1] = getPrompt(sfStr)
    data[0][2] = "null"

    #for each atom
        #find parent text
        #get atom text
        #get stance
    atoms = sf.list_atoms()

    for i in range(1,len(atoms)):
        #find parent text for atom
        connections = sf.get_connections(atoms[i]["id"])
        #loop through connections
            #if connection.sourceID = atoms[i]["id"]
                #parentTargetID = connection[targetID]
        for con in connections:
            if(con["source_id"] == atoms[i]["id"]):
               targetID = con["target_id"]
        
        #loop through edges
            #if edge.targetID = parentTargetID
                #parentID = edge.sourceID
        edges = sfJSON["edges"]
        for edge in edges:
            if(edge["source_id"] == targetID):
                parentID = edge["target_id"]
        
        #get atom text for parentID
        parent = sf.get_atom_text(parentID)

        #get atom text
        text = sf.get_atom_text(atoms[i]["id"])
        
        #get stance
        #loop through connections
        #if connection.sourceID = id
            #get target ID
        for con in connections:
            if(con["source_id"] == atoms[i]["id"]):
                targetID = con["target_id"]

        #get name for target id
        stanceAtom = sf.get_atom(targetID)
        stance = stanceAtom["name"]
        
        data[i][0] = parent
        data[i][1] = text
        data[i][2] = stance 


    return data    

#add argument
#argument = array with title, parent argument, pro/con, text
#returns status
def addArgument(argArr):
    #split argument array into parts
    prompt = argArr[0]
    newArgument = argArr[1]
    parent = argArr[2]
    stance = argArr[3]
    print(argArr)
    #get sf doc
    sfStr = fm.getFile(prompt+".json")
    sfJSON = json.loads(sfStr)
    sf.set_doc(sfJSON)
    #sf.prettyprint()

    #deal with parent argument being the debate prompt
    if(parent == "newReply"):
        parent = prompt
    
    #create argument
    if(stance == "agree"):
        sf.add_support(None, [newArgument], sf.get_atom_id(parent), None)
    if(stance == "disagree"):
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