from random import randint

code_length = 4

possibilities = ["a", "b", "c", "d", "e", "f"]
print(possibilities)

code = []

for _ in range(code_length):
    index = randint(0, len(possibilities)-1)
    value = possibilities[index]

    code.append(value)
    
print(code)

guess = input("Devinez le code à "+str(code_length)+" lettres : ")

while len(guess) != 4:
    print("Pas le bon nombre de lettres !")
    guess = input("Donnez moi un code à "+str(code_length)+" lettres :")

print("C'est la bonne longueur !")

guess = list(guess)
print(guess)