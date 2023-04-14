numbers = [1, 2, 4, 5, 1, 2, 4, 1, 4, 5]
print(numbers)

number = input("Entrez un nombre entre 1 et 5 : ")
number = int(number)

numbers.remove(number)

print(numbers)