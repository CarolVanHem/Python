from random import randint

solution = randint(1, 10)

guess = None

while guess != solution:
    guess = input("Donne un nombre de 1 & 10 : ")
    guess = int(guess)

    if guess < solution:
        print("Votre nombre est trop petit.")
    elif guess > solution:
        print("Votre nombre est trop grand.")
    else:
        print("Bravo!")