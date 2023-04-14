grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# for line in range(3):
#     txt = ""
#     for column in range(4):
#         txt = txt + str(grid[line][column])
#     print(txt + "\n")

for line in range(3):
    result = ""
    for column in range(4):    
        result = result + " " + str(grid[line][column]/2)
    print(result)