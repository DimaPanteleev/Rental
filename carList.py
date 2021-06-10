from generalList import GeneralList


class CarList(GeneralList):
    def getBrand(self, code):
        return self.findByCode(code).getBrand()

    def getPrice(self, code):
        return self.findByCode(code).getPrice()

    def getCost(self, code):
        return self.findByCode(code).getRentalPrace()

    def getCartype(self, code):
        return self.findByCode(code).getCartype()

    def getListCarstr(self):
        s = ''
        for code in self.getCodes():
            s += self.findByCode(code).getCarstr() + ',\n'
        return s
