


def initialize():
    print("Enter the grid size of the game")
    grid_no = int(input())
    
    while True:
        print("Enter the players names")
        player1 = input("Player 1: ")
        player2 = input("Player 2: ")
        
        if player1 != player2:
            break
        else:
            print("player names must be unique! please try again")
        
    #Assign characters to the players
    print(f"{player1} is X and {player2} is O")
    return grid_no , player1 , player2
    
def display():
    grid_no , player1 , player2 = initialize()
    grid = [[" " for _ in range(grid_no )] for _ in range(grid_no)]
    
    current_player = player1
    current_mark = "X"
    
    while True:
        print("\n".join([" | ".join(row) for row in grid]))
        n = input(f"{current_player}, enter your location : ").split(",")
        
        if len(n) != 2:
            print("please enter a valid location")
            continue
            
        row , col = int(n[0]) , int(n[1])
        
        if row < 1 or row > grid_no or col < 1 or col > grid_no:
            print(f"Invalid Input")
            continue
            
        row -= 1
        col -= 1
        
        if grid[row][col] != " ":
            print("Location already filled . Try again.")
            continue
        
        grid[row][col] = current_mark
        game_state = check_game_state(grid, current_mark , grid_no)
        
        if game_state == f"{current_mark} wins":
            print("\n".join([" | ".join(row) for row in grid]))
            print(f"{current_player} wins!")
            break
            
        elif game_state == "draw":
            print("\n".join([" | ".join(row) for row in grid]))
            print("its a draw!")
            break
            
        if current_player == player1:
            current_player , current_mark = player2, "O"
        else:
            current_player , current_mark = player1, "X"
            
def check_game_state(grid, mark, grid_no):
    
    for i in range(grid_no):
        if all([grid[i][j] == mark for j in range(grid_no)]) or all([grid[j][i] == mark for j in range(grid_no)]):
            return f"{mark} wins"
        if all([grid[i][i] == mark for i in range(grid_no)]) or all([grid[i][grid_no -1 -i] == mark for i in range(grid_no)]):
            return f"{mark} wins"
        if all([cell != " " for row in grid for cell in row]):
            return "draw"
        
        return None
        
display()
    
        
    
    

	
	
	
