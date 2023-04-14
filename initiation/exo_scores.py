scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

new_pseudo = input("Quel est votre pseudo : ")
score = input("Quel est votre score : ")
score = int(score)

scores[new_pseudo] = score

print(scores["Elocin03"])
print(scores[new_pseudo])