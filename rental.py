from carListEdit import CarListEdit
from clientListEdit import ClientListEdit
from activecarListEdit import ActiveCarListEdit


class Rental:
    def __init__(self):
        self.__cars = CarListEdit()
        self.__clients = ClientListEdit()
        self.__activeCars = ActiveCarListEdit()

    # Методы удаления и очистки
    def removeCar(self, id):
        self.__cars.removeList(id)
        for c in self.__cars.getIDs():
            if self.getActiveCarCarID(c) == id:
                self.__cars.setCar(c, None)

    def removeClient(self, id):
        self.__clients.removeList(id)
        for c in self.__clients.getIDs():
            if self.getActiveCarClientID(c) == id:
                self.__clients.setClient(c, None)

    def clear(self):
        self.__cars.clear()
        self.__clients.clear()
        self.__activeCars.clear()

    # Методы для авто
    def newCar(self, id=0, brand='', price='', cost='', cartype=''):
        self.__cars.newRecord(id, brand, price, cost, cartype)

    def findCarByID(self, id):
        return self.__cars.findByID(id)

    def getCarNewID(self):
        return self.__cars.getNewID()

    def getCarIDs(self):
        return self.__cars.getIDs()
        # Геттеры

    def getCarBrand(self, id):
        return self.__cars.getBrand(id)

    def getCarPrice(self, id):
        return self.__cars.getPrice(id)

    def getCarCost(self, id):
        return self.__cars.getCost(id)

    def getCarCartype(self, id):
        return self.__cars.getCartype(id)
        # Сеттеры

    def setCarBrand(self, id, value):
        self.__cars.setBrand(id, value)

    def setCarPrice(self, id, value):
        self.__cars.setPrice(id, value)

    def setCarCost(self, id, value):
        self.__cars.setCost(id, value)

    def setCarCartype(self, id, value):
        self.__cars.setCartype(id, value)

    # Методы для клиентов

    def newClient(self, id=0, surname='', name='', middlename='', address='', phone=''):
        self.__clients.newRecord(id, surname, name, middlename, address, phone)

    def findClientByID(self, id):
        return self.__clients.findByID(id)
        # Геттеры

    def getClientNewCode(self):
        return self.__clients.getNewID()

    def getClientIDs(self):
        return self.__clients.getIDs()

    def getClientSurname(self, id):
        return self.__clients.getSurname(id)

    def getClientName(self, id):
        return self.__clients.getName(id)

    def getClientMiddlename(self, id):
        return self.__clients.getMiddlename(id)

    def getClientAddress(self, id):
        return self.__clients.getAddress(id)

    def getClientPhone(self, id):
        return self.__clients.getPhone(id)

        # Сеттеры
    def setClientSurname(self, id, value):
        self.__clients.getSurname(id, value)

    def setClientName(self, id, value):
        self.__clients.getName(id, value)

    def setClientMiddlename(self, id, value):
        self.__clients.getMiddlename(id, value)

    def setClientAddress(self, id, value):
        self.__clients.getAddress(id, value)

    def setClientPhone(self, id, value):
        self.__clients.getPhone(id, value)

    # Методы для активных авто

    def removeActiveCar(self, id):
        self.__activeCars.removeList(id)

    def newActiveCar(self, id=0, car='', client='', dateOfTake='', dateOfReturn=''):
        self.__activeCars.newRecord(id, car, client, dateOfTake, dateOfReturn)

    def findActiveCarByID(self, id):
        return self.__activeCars.findByID(id)

        # Геттеры
    def getActiveCarIDs(self):
        return self.__activeCars.getIDs()

    def getActiveCarNewID(self):
        return self.__activeCars.getNewID()

    def getActiveCarDateOfTake(self, id):
        return self.__activeCars.getDateOfTake(id)

    def getActiveCarDateOfReturn(self, id):
        return self.__activeCars.getDateOfReturn(id)
        # Геттеры(авто)

    def getActiveCarCarID(self, id):
        return self.__activeCars.getCarID(id)

    def getActiveCarCarBrand(self, id):
        return self.__activeCars.getCarBrand(id)

    def getActiveCarCarPrice(self, id):
        return self.__activeCars.getCarPrice(id)

    def getActiveCarCarCost(self, id):
        return self.__activeCars.getCarCost(id)

    def getActiveCarCarCartype(self, id):
        return self.__activeCars.getCarCartype(id)
        # Геттеры(клиенты)

    def getActiveCarClientID(self, id):
        return self.__activeCars.getClientID(id)

    def getActiveCarClientSurname(self, id):
        return self.__activeCars.getClientSurname(id)

    def getActiveCarClientName(self, id):
        return self.__activeCars.getClientName(id)

    def getActiveCarClientMiddlename(self, id):
        return self.__activeCars.getClientMiddlename(id)

    def getActiveCarClientAddress(self, id):
        return self.__activeCars.getClientAddress(id)

    def getActiveCarClientPhone(self, id):
        return self.__activeCars.getClientPhone(id)
        # Сеттеры

    def setActiveCarCar(self, id, value):
        self.__activeCars.setCar(id, self.findCarByID(value))

    def setActiveCarClient(self, id, value):
        self.__activeCars.setClient(id, self.findClientByID(value))

    def setActiveCarDateOfTake(self, id, value):
        self.__activeCars.setDateOfTake(id, value)

    def setActiveCarDateOfReturn(self, id, value):
        self.__activeCars.setDateOfReturn(id, value)

    # Получение строки
    def getActiveCarstr(self, id):
        return self.__activeCars.getActiveCarstr(id)
