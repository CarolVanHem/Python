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

class Train(Vehicule):

    def __init__(self, max_capacity):
        super().__init__(150)
        self.passengers = 0 
        self.max_capacity = max_capacity

    def take_on_board(self, new_passengers):
        
        self.passengers += new_passengers
        self.passengers = min(self.passengers, self.max_capacity)

class TrainInterCity(Train):
    
    def __init__(self):
        super().__init__(100)

class FreightTrain(Train):
    
    def __init__(self):
        super().__init__(4)

