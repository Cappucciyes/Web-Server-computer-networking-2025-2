import json


class DataHandler:
    _dbPath = "./db/"

    def __init__(self):
        pass

    def addNewEntry(self, newId, newName):
        newEntry = {"id": newId, "name": newName}
        try:
            with open(self._dbPath + "{}.json".format(newId), "x") as fp:
                json.dump(newEntry , fp, indent=4) 
        except:
            print("id:{} already exists".format(newId))
            raise

    def editEntry(self, id, newName): 
        try:
            data = self.getEntry(id) 
        except:
            print("failed to get data in editEntry")
            raise

        data["name"] = newName
        with open(self._dbPath + "{}.json".format(id), "w") as fp:
            json.dump(data, fp, indent=4) 
    
    def getEntry(self, id):
        try:
            with open(self._dbPath + "{}.json".format(id), "r") as fp:
                data = json.load(fp) 
        except:
            print("id:{} does not exists".format(id))
            raise
        
        return data

if __name__ == "__main__":
    test = DataHandler() 

    test.addNewEntry(1234, "meme")

    testinput = input()
    test.editEntry(1234, testinput)
    test.editEntry(3456, testinput)

