class Animal:

    def __init__(self):
        self.happiness = 5
        self.hunger = 0

    def feed(self):
        self.hunger -= 2
        self.hunger = max(self.hunger, 0)

        # if self.hunger < 0 :
        #     self.hunger = 0

    def pet(self) :
        self.happiness += 3
        self.happiness = min(self.happiness, 10)

        # if self.happiness > 10 :
        #     self.happiness = 10 

        self.hunger += 1
        self.hunger = min(self.hunger, 10)

        # if self.hunger > 10 :
        #     self.hunger = 10


# ----- MAIN -----

animal = Animal()

animal.pet()
animal.pet()
animal.pet()
animal.feed()
animal.feed()

print(f"Happiness : {animal.happiness}/10")
print(f"Hunger : {animal.hunger}/10")