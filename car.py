from general import General


class Car(General):
    def __init__(self, id=0, brand='', price='', cost='', cartype=''):
        General.__init__(self, id)
        self.setBrand(brand)
        self.setPrice(price)
        self.setCost(cost)
        self.setCartype(cartype)

    # Геттеры
    def getID(self):
        return self.__id

    def getBrand(self):
        return self.__brand

    def getPrice(self):
        return self.__price

    def getCost(self):
        return self.__cost

    def getCartype(self):
        return self.__cartype

    # Сеттеры
    def setID(self, value):
        self.__id = value

    def setBrand(self, value):
        self.__brand = value

    def setPrice(self, value):
        self.__price = value

    def setCost(self, value):
        self.__cost = value

    def setCartype(self, value):
        self.__cartype = value

    def __str__(self):
        return "{} | {} | {} | {} | {}".format(self.__id, self.__brand, self.__price,
                                               self.__cost, self.__cartype)

    def getCarstr(self):
        s = self.getBrand()

        if self.getPrice():
            s += ' %s.' % (self.getPrice(),)
        if self.getCost():
            s += ' %s.' % (self.getCost(),)
        if self.getCartype():
            s += ' %s.' % (self.getCartype(),)

        return s
