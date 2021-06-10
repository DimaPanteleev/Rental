import os
import xml.dom.minidom
from data import Data


class Dataxml(Data):
    # Чтение
    def read(self):
        dom = xml.dom.minidom.parse(self.getInp())
        dom.normalize()

        for node in dom.childNodes[0].childNodes:
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'car'):
                id, brand, price, cost, cartype = 0, "", "", "", ""
                for t in node.attributes.items():
                    if t[0] == "id":
                        id = int(t[1])
                    if t[0] == "brand":
                        brand = t[1]
                    if t[0] == "price":
                        price = t[1]
                    if t[0] == "cost":
                        cost = t[1]
                    if t[0] == "cartype":
                        cartype = t[1]
                self.getLib().newCar(id, brand, price, cost, cartype)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'client'):
                id, surname, name, middlename, address, phone = 0, "", "", "", "", ""
                for t in node.attributes.items():
                    if t[0] == "id":
                        id = int(t[1])
                    if t[0] == "surname":
                        surname = t[1]
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "middlename":
                        middlename = t[1]
                    if t[0] == "address":
                        address = t[1]
                    if t[0] == "phone":
                        phone = t[1]
                self.getLib().newClient(id, surname, name, middlename, address, phone)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'activeCar'):
                id, car, client, dateOfTake, dateOfReturn = 0, None, None, "", ""
                for t in node.attributes.items():
                    if t[0] == "id":
                        id = int(t[1])
                    if t[0] == "car":
                        car = self.getLib().findCarByID(int(t[1]))
                    if t[0] == "client":
                        client = self.getLib().findClientByID(int(t[1]))
                    if t[0] == "dateOfTake":
                        dateOfTake = t[1]
                    if t[0] == "dateOfReturn":
                        dateOfReturn = t[1]
                self.getLib().newActiveCar(id, car, client, dateOfTake, dateOfReturn)

    def write(self):
        dom = xml.dom.minidom.Document()
        root = dom.createElement("library")
        dom.appendChild(root)

        for c in self.getLib().getCarIDs():
            car = dom.createElement("car")
            car.setAttribute('id', str(c))
            car.setAttribute('brand', self.getLib().getCarBrand(c))
            car.setAttribute('price', self.getLib().getCarPrice(c))
            car.setAttribute('cost', self.getLib().getCarCost(c))
            car.setAttribute('cartype', self.getLib().getCarCartype(c))
            root.appendChild(car)
        for c in self.getLib().getClientIDs():
            cl = dom.createElement("client")
            cl.setAttribute('id', str(c))
            cl.setAttribute('surname', self.getLib().getClientSurname(c))
            cl.setAttribute('name', self.getLib().getClientName(c))
            cl.setAttribute('middlename', self.getLib().getClientMiddlename(c))
            cl.setAttribute('address', self.getLib().getClientAddress(c))
            cl.setAttribute('phone', self.getLib().getClientPhone(c))
            root.appendChild(cl)
        for c in self.getLib().getActiveCarIDs():
            ac = dom.createElement("activeCar")
            ac.setAttribute('id', str(c))
            ac.setAttribute('car', str(self.getLib().getActiveCarCarID(c)))
            ac.setAttribute('client', str(
                self.getLib().getActiveCarClientID(c)))
            ac.setAttribute(
                'dateOfTake', self.getLib().getActiveCarDateOfTake(c))
            ac.setAttribute(
                'dateOfReturn', self.getLib().getActiveCarDateOfReturn(c))
            root.appendChild(ac)

        f = open(self.getOut(), "w")
        f.write(dom.toprettyxml())
