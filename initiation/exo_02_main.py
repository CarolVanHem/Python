from exo_02_secondary import min_max_avg

numbers = [31, 5, 12]

metadata = min_max_avg(numbers)

print(f"Plus grande valeur : {metadata['max']}")
print(f"Plus petite valeur : {metadata['min']}")
print(f"Valeur moyenne : {metadata['avg']}")