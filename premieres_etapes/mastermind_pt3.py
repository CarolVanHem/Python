fruits = ["apple", "banana", "pear", "pineapple", "peach", "avocado"]
last_index_fruits = len(fruits) -1

index = input("Entrez un nombre entre 0 et " + str(last_index_fruits) + ": ")
index = int(index)

while index < 0 or index > last_index_fruits:
    print("Erreur!")
    index = input("Entrez un nombre entre 0 et " + str(last_index_fruits) + ": ")
    index = int(index)


print(fruits)
print(fruits[:index])
print(fruits[index:])
