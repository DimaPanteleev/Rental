from general import General


class ActiveCar:
    def __init__(self, id=0, car=None, client=None, dateOfTake='', dateOfReturn=''):
        General.__init__(self, id)
        self.setCar(car)
        self.setClient(client)
        self.setDateOfTake(dateOfTake)
        self.setDateOfReturn(dateOfReturn)

    # Геттеры
    def getID(self):
        return self.__id

    def getDateOfTake(self):
        return self.__dateOfTake

    def getDateOfReturn(self):
        return self.__dateOfReturn

    # Сеттеры
    def setID(self, value):
        self.__id = value

    def setCar(self, value):
        self.__car = value

    def setClient(self, value):
        self.__client = value

    def setDateOfTake(self, value):
        self.__dateOfTake = value

    def setDateOfReturn(self, value):
        self.__dateOfReturn = value

    # Методы для классов Car и Client
    def getClientID(self):
        if self.__client:
            return self.__client.getID()

    def getClientSurname(self):
        if self.__client:
            return self.__client.getSurname()

    def getClientName(self):
        if self.__client:
            return self.__client.getName()

    def getClientMiddlename(self):
        if self.__client:
            return self.__client.getMiddlename()

    def getClientAddress(self):
        if self.__client:
            return self.__client.getAddress()

    def getClientPhone(self):
        if self.__client:
            return self.__client.getPhone()

    def getCarID(self):
        return self.__car.getID()

    def getCarBrand(self):
        return self.__car.getBrand()

    def getCarPrice(self):
        return self.__car.getPrice()

    def getCarCost(self):
        return self.__car.getCost()

    def getCarCartype(self):
        return self.__car.getCartype()

    def getActiveCarstr(self):
        s = ''

        if self.__car:
            scar = self.getCarBrand()
        else:
            scar = ''

        if self.__client:
            sclient = self.getClientName()
        else:
            sclient = ''

        s = ' ID: %s %s %s, %s - %s' % (self.getID(), scar, sclient,
                                        str(self.getDateOfTake()), str(self.getDateOfReturn()))
        return s
