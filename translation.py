import sadface as sf

#method to read in form SADFace doc and take variables out
def getArguments():
    sf.config.init("SADFace/test.cfg")
    #sf.initialise()
    #import document to sf
    f = sf.new_sadface()
    f = sf.load_from_file("saves.json")
    fa = sf.list_arguments()
    print(fa)
    #list_atoms
    return None


test = getArguments()