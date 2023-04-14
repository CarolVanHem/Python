class Calcultator:
    
    def __init__(self, value):
        self.result = value
    
    def add(self, value):
        self.result += value

# ----- MAIN -----

calc = Calcultator(6)
calc.add(3)
print(calc.result)
