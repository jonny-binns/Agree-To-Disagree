import unittest
import sadface as sf
import fileManager as fm
import translation as t
import os
#document contains the unit tests for Agree to Disagree

#creates the bare minimum SF doc for test_createFile()
def createTestFile():
    sf.initialise()
    sf.set_title("test file")
    return sf.export_json()


#creates the array of argument data needed for test_addArgument()
def createArgArr():
    #will add arguments to the file created in test_addPrompt()
    prompt = "test prompt"
    newArgument = "test argument"
    parent = "test prompt"
    stance = "agree"
    argArr = [prompt, newArgument, parent, stance]
    return argArr


class TestMakeFiles(unittest.TestCase):
    #tests the methods that make files and the method that deletes them

    def test_createFile(self): 
        #checks response to fm.createFile is None
        self.assertIsNone(fm.createFile(createTestFile()))

    def test_addPrompt(self):
        #checks the response to t.addPrompt() is none
        prompt = "test prompt"
        self.assertIsNone(t.addPrompt(prompt))

    def test_deleteFile(self):
        self.assertIsNone(fm.deleteFile("test file"))
        self.assertIsNone(fm.deleteFile("test prompt"))

    


class Tests(unittest.TestCase):

    def setUp(self):
        argArr = createArgArr()
        prompt = argArr[0]
        t.addPrompt(prompt)
    

    def test_getPrompt(self):
        sfStr = fm.getFile("test prompt.json")
        returnedPrompt = t.getPrompt(sfStr)
        correctPrompt = "test prompt"
        self.assertEqual(returnedPrompt, correctPrompt)


    #getArguments is not currently in use
    def test_getArguments(self):
        sfStr = fm.getFile("test prompt.json")
        self.assertIsNotNone(t.getArguments(sfStr))


    def test_getData(self):
        sfStr = fm.getFile("test prompt.json")
        returnedData = t.getData(sfStr)
        correctData = [['null', 'test prompt', 'null']]
        self.assertEqual(returnedData, correctData)


    def test_addArgument(self):
        argArr = createArgArr()
        self.assertIsNone(t.addArgument(argArr))


    def test_getRandomFile(self):
        result = fm.getRandomFile()
        self.assertIsNotNone(result)


    def test_getFile(self):
        self.assertIsNotNone(fm.getFile("test prompt.json"))


    def tearDown(self):
        fm.deleteFile("test prompt")



if __name__ == '__main__':
    unittest.main()