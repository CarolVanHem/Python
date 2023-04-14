class Fruit :

    def __init__(self, name, nutritional_value):
        self.name = name
        self.nutritional_value = nutritional_value

class Kirky :

    def __init__(self):
        self.hp = 1
        self.weight = 1

    def eat(self, fruit):
        self.hp += fruit.nutritional_value 
        self.weight += 1


# ---- main ----

kirky = Kirky()
banana = Fruit("Banana", 2)

kirky.eat(banana)

print(banana.nutritional_value)
print(kirky.hp)

