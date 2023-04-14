from random import randint

solution = randint(1, 10)

guess = None

tries = 3

while guess != solution and tries > 0:
    guess = input("Choisissez un nombre de 1 & 10 : ")
    guess = int(guess)
    tries = tries - 1

    if guess < solution:
        print("Votre nombre est trop petit.")
    elif guess > solution:
        print("Votre nombre est trop grand.")
    
if guess == solution:
    print("Bravo!")
else:
    print("Raté... c'était " + str(solution))