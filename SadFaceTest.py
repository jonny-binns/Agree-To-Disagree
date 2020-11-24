import json
import sadface as sf

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
sf.add_conflict(None, sf.get_atom_id("The beatles are the best band of all time"), oppose, None)


print(sf.prettyprint())
#dot = sf.export_dot()#trad=False)    # Uncomment to use the brewer colourscheme
#with open('out.dot', 'w') as file:
    #file.write(dot)

sf.save("saves", "json")