import os
import sqlite3 as db
from data import Data

emptydb = """
PRAGMA foreign_keys = ON;

create table car(
  id integer primary key,
  brand text,
  price integer,
  cost integer,
  cartype text
);

create table client(
  id integer primary key,
  surname text,
  name text,
  middlename text,
  address text,
  phone text
);

create table activeCar(
  id integer primary key,
  car integer references car(id) on update cascade on delete set null,
  client integer references client(id) on update cascade on delete set null,
  dateOfTake text,
  dateOfReturn text
);
"""


class Datasql(Data):
    # Чтение
    def read(self):
        conn = db.connect(self.getInp())
        curs = conn.cursor()

        curs.execute('select id, brand, price, cost, cartype from car')
        data = curs.fetchall()
        for r in data:
            self.getLib().newCar(r[0], r[1], r[2], r[3], r[4])

        curs.execute(
            'select id, surname, name, middlename, address, phone from client')
        data = curs.fetchall()
        for r in data:
            self.getLib().newClient(r[0], r[1], r[2], r[3], r[4], r[5])

        curs.execute(
            'select id, car, client, dateOfTake, dateOfReturn from activeCar')
        data = curs.fetchall()
        for r in data:
            self.getLib().newActiveCar(r[0], r[1], r[2], r[3], r[4])

        conn.close()

    # Запись
    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)
        for c in self.getLib().getCarIDs():
            curs.execute("insert into car(id, brand, price, cost, cartype) values('%s','%s','%s','%s','%s')" % (str(c),
                                                                                                                self.getLib().getCarBrand(c),
                                                                                                                str(self.getLib(
                                                                                                                ).getCarPrice(c)),
                                                                                                                str(self.getLib(
                                                                                                                ).getCarCost(c)),
                                                                                                                self.getLib().getCarCartype(c)))
        for c in self.getLib().getClientIDs():
            curs.execute("insert into client(id, surname, name, middlename, address, phone) values('%s','%s','%s','%s','%s','%s')" % (str(c),
                                                                                                                                      self.getLib().getClientSurname(c),
                                                                                                                                      self.getLib().getClientName(c),
                                                                                                                                      self.getLib().getClientMiddlename(c),
                                                                                                                                      self.getLib().getClientAddress(c),
                                                                                                                                      self.getLib().getClientPhone(c)))
        for c in self.getLib().getActiveCarIDs():
            curs.execute("insert into activeCar(id, car, client, dateOfTake, dateOfReturn) values('%s','%s','%s','%s','%s')" % (str(c),
                                                                                                                                str(self.getLib(
                                                                                                                                ).getActiveCarCarID(c)),
                                                                                                                                str(self.getLib(
                                                                                                                                ).getActiveCarClientID(c)),
                                                                                                                                self.getLib().getActiveCarDateOfTake(c),
                                                                                                                                self.getLib().getActiveCarDateOfReturn(c)))
        conn.commit()
        conn.close()
