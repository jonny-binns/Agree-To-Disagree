import json
import sadface as sf
import fileManager as fm
import translation as t

#sfStr = fm.getFile("saves.json")
#arguments = t.getArguments(sfStr)
#print(arguments)

sf.config.init("SADFace/test.cfg")
sf.initialise()

sf.set_title("test argument")


#simple argument for testing

#set base statement
statement = "The beatles are the best band of all time and ive added this to see what happens if i just write over a document"
sf.add_atom(statement)
sf.set_claim(sf.get_atom_id("The beatles are the best band of all time and ive added this to see what happens if i just write over a document"))
#set supporting point
support = ["their albums rank among the highest of all time"]
sf.add_support(None, support, sf.get_atom_id("The beatles are the best band of all time and ive added this to see what happens if i just write over a document"), None)

#opposing point
oppose = "pink floyd explored more musically"
sf.add_conflict(None, oppose, sf.get_atom_id("The beatles are the best band of all time and ive added this to see what happens if i just write over a document"), None)


#dot = sf.export_dot()#trad=False)    # Uncomment to use the brewer colourscheme
#with open('out.dot', 'w') as file:
    #file.write(dot)
sf.save("saves", "json")


#sfJSON = sf.export_json()
#fm.createFile(sfJSON)