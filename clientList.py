from generalList import GeneralList


class ClientList(GeneralList):
    def getSurname(self, id):
        return self.findByCode(id).getSurname()

    def getName(self, id):
        return self.findByCode(id).getName()

    def getMiddlename(self, id):
        return self.findByCode(id).getMiddlename()

    def getAddress(self, id):
        return self.findByCode(id).getAddress()

    def getPhone(self, id):
        return self.findByCode(id).getPhone()

    def getListClientstr(self):
        s = ''
        for id in self.getCodes():
            s += self.findByCode(id).getClientstr() + ',\n'
        return s[:-2]
