from random import randint

code_length = 4

possibilities = ["a", "b", "c", "d", "e", "f"]
print(possibilities)

code = []

while len(code) < code_length:
    index = randint(0, len(possibilities)-1)
    value = possibilities[index]

    code.append(value)

print(code)