from random import randint

def lettre_hasard():
    lettres = ["a", "b", "c", "d", "e"]
    index = randint(0, len(lettres) - 1)
    return lettres[index]

word = ""

for _ in range(5):
    word = word + lettre_hasard()

print(word)