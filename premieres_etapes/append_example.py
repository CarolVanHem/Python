words = []

new_word = input("Entrez un mot (\"stop\" pour finir) :")

while new_word != "stop":
    words.append(new_word)
    new_word = input("Entrez un mot (\"stop\" pour finir) :")

print(words)