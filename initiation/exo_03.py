class Flower :
    
    def __init__(self):
        self.growth = 0
        self.price = 5

    def water(self):
        self.growth += 1
        return self.growth

# ----- MAIN -----

flower = Flower()
print(f"Prix de la fleur : {flower.price}")
flower.water()
flower.water()    
print(f"Niveau de croissance : {flower.growth}")