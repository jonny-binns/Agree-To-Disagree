import sadface as sf
from argument import Argument
import json

#method to read in form SADFace doc and take variables out
def getArguments():
    sf.initialise()
    x = sf.load_from_file("saves.json")
    #use import json
    sf.sd = sf.import_json(x)
    print()

    return None



#main bit
getArguments()