class Bike :

    def __init__(self) :
        self.speed = 15
        self.distance = 0
    
    def ride(self, time):
        self.distance += time * self.speed
        
class Car :

    def __init__(self):
        self.speed = 100
        self.distance = 0
    
    def ride (self, time):
        self.distance += time * self.speed


