from activecar import ActiveCar
from generalListEdit import GeneralListEdit


class ActiveCarListEdit(GeneralListEdit):
    def newRecord(self, id=0, car=None, client=None, dateOfTake='', dateOfReturn=''):
        self.appendList(ActiveCar(id, car, client, dateOfTake, dateOfReturn))

    # Сеттеры
    def setCar(self, id, value):
        self.findByID(id).setCar(value)

    def setClient(self, id, value):
        self.findByID(id).setClient(value)

    def setDateOfTake(self, id, value):
        self.findByID(id).setDateOfTake(value)

    def setDateOfReturn(self, id, value):
        self.findByID(id).setDateOfReturn(value)

    # Геттеры
    def getCar(self, id):
        return self.findByID(id).getCar()

    def getClient(self, id):
        return self.findByID(id).getClient()

    def getDateOfTake(self, id):
        return self.findByID(id).getDateOfTake()

    def getDateOfReturn(self, id):
        return self.findByID(id).getDateOfReturn()

    # Методы для Car и Client
    def getCarID(self, id):
        return self.findByID(id).getCarID()

    def getCarBrand(self, id):
        return self.findByID(id).getBrand()

    def getCarPrice(self, id):
        return self.findByID(id).getPrice()

    def getCarCost(self, id):
        return self.findByID(id).getCost()

    def getCarCartype(self, id):
        return self.findByID(id).getCartype()

    def getClientID(self, id):
        return self.findByID(id).getClientID()

    def getClientSurname(self, id):
        return self.findByID(id).getClientSurname()

    def getClientName(self, id):
        return self.findByID(id).getClientName()

    def getClientMiddlename(self, id):
        return self.findByID(id).getClientMiddlename()

    def getClientAddress(self, id):
        return self.findByID(id).getClientAddress()

    def getClientPhone(self, id):
        return self.findByID(id).getClientPhone()

    def getActiveCarstr(self, id):
        return self.findByID(id).getActiveCarstr()
