from random import randint

def dice():
    result = randint(1, 6)
    return result

value = dice()
print(value)