class Flower :
    
    def __init__(self):
        self.growth = 0
        self.price = 5
        self.sprinkles = 0

    def water(self):

        self.sprinkles += 1

        if self.sprinkles % 3 == 0 :
            if self.growth < 3 :
                self.growth += 1

    def sell(self):
        return self.price * self.growth


# ----- MAIN -----


flower = Flower()

while flower.growth < 3:
    flower.water()
    
print(f"Nombre d'arrosage(s) : {flower.sprinkles}")
print(f"Niveau de croissance : {flower.growth}")
print(f"Prix de la fleur : {flower.sell()}")