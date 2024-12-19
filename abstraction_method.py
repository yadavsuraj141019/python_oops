from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def mileage(self):
        pass

    def color(self):
        print("white")

class Maruti_Suzuki(Car):
    
    def mileage(self):
        print("mileage is 30 kmph")


class Tata(Car):

    def mileage(self):
        print("mileage is 40 kmph")

class Duster(Car):

    def mileage(self):
        print("mileage is 45 kmph")

m=Maruti_Suzuki()
t=Tata()
d=Duster()

m.mileage()