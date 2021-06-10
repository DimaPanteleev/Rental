from rental import Rental
from dataxml import Dataxml
from datasql import Datasql
import os

rent1 = Rental()
rent2 = Rental()

dxml1 = Dataxml(rent1, 'old.xml', 'new.xml')
dxml2 = Dataxml(rent2, 'old.xml', 'new.xml')

dsql1 = Datasql(rent1, 'new.sqlite', 'new.sqlite')

dxml1.read()
if os.path.isfile(dsql1.getOut()):
    os.remove(dsql1.getOut())

dsql1.write()
dsql1.read()
dxml2.write()
