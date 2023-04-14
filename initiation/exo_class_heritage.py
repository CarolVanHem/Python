class Vehicule :

    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    
    def ride (self, time):
        self.distance += time * self.speed

class Bike(Vehicule) :

    def __init__(self):
        super().__init__(15)

class Car(Vehicule) : 
    
    def __init__(self):
        super().__init__(100)

# ---- MAIN ----

bike = Bike()
car = Car()

car.ride(2)
bike.ride(2)

print(f"distance parcourue : {car.distance}")
print(f"distance parcourue : {bike.distance}")

