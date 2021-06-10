from car import Car
from generalListEdit import GeneralListEdit


class CarListEdit(GeneralListEdit):
    # Новая запись
    def newRecord(self, id=0, brand='', price='', cost='', cartype=''):
        self.appendList(Car(id, brand, price, cost, cartype))

    # Сеттеры
    def setBrand(self, id, value):
        self.findByID(id).setBrand(value)

    def setPrice(self, id, value):
        self.findByID(id).setPrice(value)

    def setCost(self, id, value):
        self.findByID(id).setCost(value)

    def setType(self, id, value):
        self.findByID(id).setType(value)

    # Геттеры
    def getBrand(self, id):
        return self.findByID(id).getBrand()

    def getPrice(self, id):
        return self.findByID(id).getPrice()

    def getCost(self, id):
        return self.findByID(id).getCost()

    def getCartype(self, id):
        return self.findByID(id).getCartype()
