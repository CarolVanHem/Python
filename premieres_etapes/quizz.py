print("Boisson favorite ?")
print("1 - Eau")
print("2 - Café")
print("3 - Thé")

answer = input("Choisissez 1, 2 ou 3 : ")
answer = int(answer)

if answer == 1:
    print("Eau, top!")
elif answer == 2:
    print("Café!!!")
else:
    print("Hééé")
