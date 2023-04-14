words = []

new_word = input("Entrez un mot (\"stop\" pour finir) :")

while new_word != "stop":
    index = input("Entrez l'index où le mot doit être inséré :")
    index = int(index)
    words.insert(index, new_word)
    new_word = input("Entrez un autre mot (\"stop\" pour finir) :")

print(words)