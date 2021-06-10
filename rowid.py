class RowID:
    def __init__(self):
        self.__list = []

    def clear(self):
        self.__list = []

    def appendRowID(self, row, id):
        self.__list.append([row, id])

    # Методы для строк данных
    def updateRow(self, row):
        for t in self.__list:
            if t[0] > row:
                t[0] -= 1

    def removeRow(self, row):
        for t in self.__list:
            if t[0] == row:
                self.__list.remove(t)
        self.updateRow(row)

    def getRow(self, id):
        for t in self.__list:
            if t[1] == id:
                return t[0]

    # Методы для id
    def removeID(self, id):
        for t in self.__list:
            if t[1] == id:
                self.__list.remove(t)

    def getID(self, row):
        for t in self.__list:
            if t[0] == row:
                return t[1]

    def getIDs(self):
        return [t[1] for t in self.__list]
