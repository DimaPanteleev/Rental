from PyQt5.QtWidgets import QTableWidget
from rowid import RowID
from rentwidget import RentWidget


class DBTableWidget(QTableWidget, RentWidget):
    def __init__(self, rental, parent=None, header=[]):
        QTableWidget.__init__(self)
        RentWidget.__init(self, rental)
        self.__rowID = RowID()
        self.setHeader(header)
        self.update()

    def setHeader(self, value):
        self.setColumnCount(len(value))
        self.setHorizontalHeaderLabels(value)

    def clearContents(self):
        self.__rowID.clear()
        QTableWidget.clearContents(self)

    def getIDs(self):
        return self.__rowID.getIDs()

    def getCurrentID(self):
        return self.__rowID.getID(self.currentID())

    def appendRowID(self, row, id):
        self.__rowID.appendRowID(row, id)

    def update(self):
        pass
