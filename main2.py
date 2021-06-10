from rental import Rental
from dataxml import Dataxml

rent1 = Rental()
dat1 = Dataxml(rent1, 'old.xml', 'new.xml')

dat1.read()
dat1.write()

for k in rent1.getActiveCarIDs():
    print(rent1.getActiveCarstr(k))
