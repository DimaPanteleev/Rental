from client import Client
from generalListEdit import GeneralListEdit


class ClientListEdit(GeneralListEdit):
    # Новая запись
    def newRecord(self, id='', surname='', name='', middlename='', address='', phone=''):
        self.appendList(Client(id, surname, name, middlename, address, phone))

    # Сеттеры
    def setSurname(self, id, value):
        self.findByID(id).setSurname(value)

    def setName(self, id, value):
        self.findByID(id).setName(value)

    def setMiddlename(self, id, value):
        self.findByID(id).setMiddlename(value)

    def setAddress(self, id, value):
        self.findByID(id).setAddress(value)

    def setPhone(self, id, value):
        self.findByID(id).setPhone(value)

    # Геттеры
    def getSurname(self, id):
        return self.findByID(id).getSurname()

    def getName(self, id):
        return self.findByID(id).getName()

    def getMiddlename(self, id):
        return self.findByID(id).getMiddlename()

    def getAddress(self, id):
        return self.findByID(id).getAddress()

    def getPhone(self, id):
        return self.findByID(id).getPhone()
