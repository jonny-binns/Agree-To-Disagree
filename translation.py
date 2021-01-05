import sadface as sf
from argument import Argument
import json

#method to read in form SADFace doc and take variables out
def getArguments():
    sfdoc = sf.load_from_file("saves.json")
    sf.set_doc(sfdoc)
    result, problems = sf.validation.verify(sf.get_document())
    if result:
        print(" ,".join(problems))
        print(sf.prettyprint())
    else:
        print(sf.prettyprint())
    return None



#main bit
getArguments()