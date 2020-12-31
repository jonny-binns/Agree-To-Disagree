"""
this whole file will need to be re-written when sadface and argdb are used
exists in order for me to work on the front end of the website with an example argument
method names should be carried accross when re-writing
"""


def getArguments():
    f = open("testArgument.txt", "r")
    fStr = f.read()
    fSplit = fStr.split(',')
    return fSplit

#write add argument
def addArgument(argument):
    f = open("testArgument.txt", "a")
    f.write("," + argument)
    f.close()
    return None
