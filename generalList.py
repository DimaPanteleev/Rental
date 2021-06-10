class GeneralList:
    def __init__(self):
        self.__list = []

    def clear(self):
        self.__list = []

    def findByID(self, id):
        for l in self.__list:
            if l.getID() == id:
                return l

    def getIDs(self):
        return [s.getID() for s in self.__list]

    def appendList(self, value):
        self.__list.append(value)

    def removeList(self, id):
        for s in self.__list:
            if s.getID() == id:
                self.__list.remove(s)
