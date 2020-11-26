import sadface as sf
from argument import Argument
import json

#method to read in form SADFace doc and take variables out
def getArguments():
    sd = sf.initialise()
    sd = sf.load_from_file("saves.json")
    sd = sf.prettyprint()
    print(sd)

    return None



#main bit
getArguments()