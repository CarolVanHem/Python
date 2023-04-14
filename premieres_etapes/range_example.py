my_sequence = range(10)
my_list = list(my_sequence)
print(my_list)

name = "thomas"
print(list(name))
print(name[3])

# slicing pour changer une lettre
name = name [:3] + "w" + name[4:]
print(name)

name = name[-1:-7:-1]
print(name)


