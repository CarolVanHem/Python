from random import randint

result = randint(1, 10)

number = input("Donne un nombre de 1 & 10 : ")
number = int(number)

if number < result:
    print(str(number) + " est plus petit que le chiffre à trouver.")
elif number > result:
    print(str(number) + " est plus grand que le chiffre à trouver.")
else:
    print(str(number) + " est le bon chiffre !")