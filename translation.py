import sadface as sf
from argument import Argument
import json

#method to read in form SADFace doc and take variables out
def getArguments():
    sfdoc = sf.load_from_file("saves.json")
    result, problems = sf.validation.verify(sf.get_document())
    if result:
        print(" ,".join(problems))
    else:
        print(sf.prettyprint())
    return None



#main bit
getArguments()