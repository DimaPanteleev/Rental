class Data:
    def __init__(self, lib=None, inp='', out=''):
        self.setLib(lib)
        self.setInp(inp)
        self.setOut(out)

    # Сеттеры
    def setLib(self, value):
        self.__lib = value

    def setInp(self, value):
        self.__inp = value

    def setOut(self, value):
        self.__out = value

    # Геттеры
    def getLib(self):
        return self.__lib

    def getInp(self):
        return self.__inp

    def getOut(self):
        return self.__out

    # Чтение и запись
    def readFile(self, filename):
        self.setInp(filename)
        self.read()

    def writeFile(self, filename):
        self.setOut(filename)
        self.write()

    def read(self):
        pass

    def write(self):
        pass
