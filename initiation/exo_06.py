class Animal:

    def __init__(self):
        self.happiness = 5
        self.hunger = 0
        self.sleepiness = 0

    def feed(self):

        if self.sleepiness >= 10 :
            return
        
        elif self.sleepiness < 10 :
            self.hunger -= 2
            self.hunger = max(self.hunger, 0)

            self.sleepiness += 1
            self.sleepiness = min(self.sleepiness, 10)

    def pet(self) :
        self.happiness += 3
        self.happiness = min(self.happiness, 10)

        self.hunger += 1
        self.hunger = min(self.hunger, 10)
      
    def play(self):
        self.happiness += 4
        self.happiness = min(self.happiness, 10)

        self.hunger += 2
        self.hunger = min(self.hunger, 10)

        self.sleepiness += 4
        self.sleepiness = min(self.sleepiness, 10)

    def need_for_sleep(self):
        self.sleepiness -= 3
        self.sleepiness = max(self.sleepiness, 0)

        self.happiness -= 2
        self.happiness = max(self.sleepiness, 0)
      

# ----- MAIN -----


animal = Animal()

while animal.sleepiness < 10:
    animal.play()

animal.pet()
animal.feed()

print(f"Happiness : {animal.happiness}/10")
print(f"Hunger : {animal.hunger}/10")