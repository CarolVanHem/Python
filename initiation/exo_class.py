class Calcultator:
    
    def __init__(self, value):
        self.result = value
    
    def add(self, value):
        self.result += value
        return self.result

    def sub(self, value):
        self.result -= value
        return self.result
    
    def mult(self, value):
        self.result *= value
        return self.result
    
    def div(self, value):
        self.result /= value
        return self.result
    
    def reset(self):
        self.result = 0

# ----- MAIN -----

calc = Calcultator(6)
print(calc.add(3))
print(calc.sub(2))
print(calc.mult(4))
print(calc.div(2))
print(calc.reset())

