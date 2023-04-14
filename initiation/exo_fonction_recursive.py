def monster_size(year):
    if year == 1:
        return 0.8
    
    return monster_size(year-1) * 1.5

print(monster_size(4))
print(monster_size(50))
