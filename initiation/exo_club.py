club = {
    "Marie": 1,
    "Bernard": 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15
}

for name, point in list(club.items()):
    if point >= 10:
        club.pop(name)

# autre façon de faire avec deux boucles for :

# members_to_be_removed = []

# for name in club:
#     if club[name] >= 10:
#         members_to_be_removed.append(name)

# for element in members_to_be_removed:
#     club.pop(element)

# print(members_to_be_removed)    
    
print (club)

total = 0

for rank in club.values():
    total = total + rank

moyenne = total / len(club)
print(moyenne)