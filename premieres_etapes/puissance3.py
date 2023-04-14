
def display_grid(grid):
 
    for line_number in range(len(grid)):
        result = str(line_number)

        for col_number in range(len(grid[0])):
            result = result + " " + grid[line_number][col_number]
        print(result)
    
    bottom_line = " "
    for col_number in range(len(grid[0])):
        bottom_line = bottom_line + " " + str(col_number)

    print(bottom_line)

def play_one_turn(grid, player):
    display_grid(tableau)

    column = input("Joueur "+ str(player) +". Quelle colonne ? ")
    column = int(column)

    #boucle while pour demander à l'utilisateur un chiffre entre 0 et 4 

    grid = place_token(grid, player, column)

    return check(grid, column)

def place_token(grid, player, column):
    
    line = 0
    
    while line <= 4 and grid[line][column] == ".":
        line = line + 1

    line = line - 1
    
    if line >= 0:
        if player == 1:
            token = "0"
        else:
            token = "X"
        grid[line][column] = token

    return grid

    # comment faire avec la boucle for :
    # for line in range(len(grid)):
    #     if grid[line][column] != ".":
    #         line = line - 1
    #         break

def check_vertical(grid, column, line):

    if line >=3:
        return False
    
    token = grid[line][column]

    if grid[line + 1][column] == token and grid[line + 2][column] == token:
        return True

    return False

def check_horizontal(grid, column, line):

    token = grid[line][column]
    
    if column <=2:
        if grid[line][column + 1] == token and grid[line][column + 2] == token:
            return True
    
    if column >= 2:
        if grid[line][column - 1] == token and grid[line][column - 2] == token:
            return True
    
    if column >= 1 and column <=3:
        if grid[line][column - 1] == token and grid[line][column + 1] == token:
            return True

    return False

def check_diagonal(grid, column, line):

    token = grid[line][column]

    if line <= 2 and column <= 2:
        if grid[line + 1][column + 1] == token and grid[line + 2][column + 2] == token:
            return True

    if line >= 2 and column >= 2:
        if grid[line - 1][column - 1] == token and grid[line - 2][column - 2] == token:
            return True

    if line >= 1 and line <= 3 and column >= 1 and column <= 3:
        if grid[line - 1][column - 1] == token and grid[line + 1][column + 1] == token:
            return True

    if line >= 2 and column <= 2:
        if grid[line - 1][column + 1] == token and grid[line - 2][column + 2] == token:
            return True

    if line <= 2 and column >= 2:
        if grid[line + 1][column - 1] == token and grid[line + 2][column - 2] == token:
            return True 

    if line >= 1 and line <= 3 and column >= 1 and column <= 3:
        if grid[line + 1][column - 1] == token and grid[line - 1][column + 1] == token:
            return True        

    return False

def check(grid, column):
    
    line = 0

    while line <= 4 and grid[line][column] == ".":
        line = line + 1

    if check_vertical(grid, column, line) == True:
        return True

    if check_horizontal(grid, column, line) == True:
        return True

    if check_diagonal(grid, column, line) == True:
        return True

    return False


tableau = [
    [".", ".", ".", ".", "."], 
    [".", ".", ".", ".", "."], 
    [".", ".", ".", ".", "."], 
    [".", ".", ".", ".", "."], 
    [".", ".", ".", ".", "."]
]

display_grid(tableau)
  
winner = None

current_player = 1

while winner == None:

    if play_one_turn(tableau, current_player) == True:
        winner = current_player
    else:
        # switch players
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

print("Félicitations joueur " + str(current_player) + " !!")
display_grid(tableau)