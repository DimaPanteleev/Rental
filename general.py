class General():
    def __init__(self, id=0):
        self.setID(id)

    def setID(self, value):
        self.__id = int(value)

    def getID(self):
        return self.__id
