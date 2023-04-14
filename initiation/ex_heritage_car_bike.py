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
        self.fuel = 100
        self.consumption = 0.05
    
    def ride(self, duration):
        super().ride(duration)
        fuel_loss = self.consumption * duration * self.speed
        self.fuel -= fuel_loss





