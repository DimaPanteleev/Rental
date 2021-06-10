from activecar import ActiveCar
from car import Car
from client import Client

a1 = ActiveCar(1, dateOfTake = "10.11.2020", dateOfReturn = "10.12.2020")
a1.setCar(Car(1, "Subaru", 2000000, 30000, "Sport"))
a1.setClient(Client(1, "Panteleev", "Dmitriy", "Alexandrovich", "Izmaylova, 5", 89271653040))

print(a1.getActiveCarstr())
