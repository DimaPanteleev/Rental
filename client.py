from general import General


class Client(General):
    def __init__(self, id=0, surname='', name='', middlename='', address='', phone=''):
        General.__init__(self, id)
        self.setSurname(surname)
        self.setName(name)
        self.setMiddlename(middlename)
        self.setAddress(address)
        self.setPhone(phone)

    # Геттеры
    def getID(self):
        return self.__id

    def getSurname(self):
        return self.__surname

    def getName(self):
        return self.__name

    def getMiddlename(self):
        return self.__middlename

    def getAddress(self):
        return self.__address

    def getPhone(self):
        return self.__phone

    # Сеттеры
    def setID(self, value):
        self.__id = value

    def setSurname(self, value):
        self.__surname = value

    def setName(self, value):
        self.__name = value

    def setMiddlename(self, value):
        self.__middlename = value

    def setAddress(self, value):
        self.__address = value

    def setPhone(self, value):
        self.__phone = value

    def __str__(self):
        return "{} | {} | {} | {} | {} | {}".format(self.__id, self.__surname, self.__name,
                                                    self.__middlename, self.__address, self.__phone)

    def getClientstr(self):
        s = self.getSurname()

        if self.getName():
            s += ' %s.' % (self.getName(),)
        if self.getMiddlename():
            s += ' %s.' % (self.getMiddlename(),)
        if self.getAddress():
            s += ' %s.' % (self.getAddress(),)
        if self.getPhone():
            s += ' %s.' % (self.getPhone(),)

        return s
