from random import randint, choice

class Fruit :

    def __init__(self, name, nutritional_value):
        self.name = name
        self.nutritional_value = nutritional_value

class Pear(Fruit):

    def __init__(self):
        super().__init__("poire", randint(1, 3))

class Apple(Fruit):

    def __init__(self):
        name = choice(["Jonagold", "Grannysmith", "Golden"])
        super().__init__(name, 2)

class Kirky :

    def __init__(self):
        self.hp = 1
        self.weight = 1

    def eat(self, fruit):
        self.hp += fruit.nutritional_value 
        self.weight += 1
        print(f"Fruit mangé : {fruit.name}")

        



# ---- MAIN ----

kirky = Kirky()

fruits = [Pear(), Pear(), Apple(), Apple()]

while fruits :
    fruit = fruits.pop()
    kirky.eat(fruit)

# raccourci pour dire tant que la liste fruits 'existe', plutot que d'écrire 'while len(fruits) > 0 :' 

print(f"Poids : {kirky.weight}")
print(f"HP : {kirky.hp}")