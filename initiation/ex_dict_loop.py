inventory = {"potion": 1, "scroll": 2, "holy sword": 0}

for key in inventory :
    print(key)
    # ou pour avoir la valeur : print(inventory[key])

for value in inventory.values():
    print(value)

for key, value in inventory.items():
    print(key + " : " + str(value))