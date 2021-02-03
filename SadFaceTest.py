import json
import sadface as sf
import fileManager as fm

sf.config.init("SADFace/test.cfg")
sf.initialise()

sf.set_title("test argument")

#simple argument for testing

#set base statement
statement = "The beatles are the best band of all time"
sf.add_atom(statement)

#set supporting point
support = ["their albums rank among the highest of all time"]
sf.add_support(None, support, sf.get_atom_id("The beatles are the best band of all time"), None)

#opposing point
oppose = "pink floyd explored more musically"
sf.add_conflict(None, oppose, sf.get_atom_id("The beatles are the best band of all time"), None)


#dot = sf.export_dot()#trad=False)    # Uncomment to use the brewer colourscheme
#with open('out.dot', 'w') as file:
    #file.write(dot)
#sf.save("saves", "json")
sfJSON = sf.export_json()
#print(sfJSON)
fm.createFile(sfJSON)