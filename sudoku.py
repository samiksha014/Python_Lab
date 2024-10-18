import random

def display(grid):
    horizontal_line = "__"*(len(grid)+1)
    print(horizontal_line)
    for row in grid:
        s = "|{}" * len(grid) + "|"
        print(s.format(*row))
        print(horizontal_line)
        
def fill_sudoku(grid_size):
    sudoku_state = [list(" " *grid_size) for _ in range(grid_size)]
    p = set(range(1,grid_size+1))
    for r in range(grid_size):
        for c in range(grid_size):
            a = set(sudoku_state[r] + [ tr[c] for tr in sudoku_state ] )
            numbers = list(p-a)
            if numbers :
                sudoku_state[r][c] = numbers.pop(random.randint(0,len(numbers)-1))
            else:
                return fill_sudoku(grid_size)
    return sudoku_state
    
def initialize():
    print("welcome to the Sudoku game!!")
    grid_size = int(input("enter the grid size: ")) 
    sudoku_state = fill_sudoku(grid_size)
    return grid_size,sudoku_state


def start_game(state):
    level_of_game = { "low": 0.2 ,  "medium": 0.3 , "hard":0.5}
    game_level =  input("Choose the Level of the game (low , medium , hard) : ").lower()
    
    if game_level not in level_of_game:
        print("Invalid level , re-enter it")
        return
    else:
        no_of_places = int(len(state)*len(state)*level_of_game[game_level])
        empty_positions = []
        
    while len(empty_positions) < no_of_places:
        row = random.randint(0,len(state)-1)
        col = random.randint(0,len(state[row])-1)
        if state[row][col] != " ":
            empty_positions.append([row,col])
            state[row][col] = " "
    display(state)
    
    while empty_positions:
            print(f"Available empty positions [row,column] : {empty_positions}")
            if len(empty_positions) == 1:
                r , c = empty_positions[0]
                print("enter the Number to be filled in the position as there is only one position to be filled")
                user_input = int(input())
                state[r][c] = user_input
                display(state)
                empty_positions.remove([r,c])
            else:
                print("Enter the empty positions index to fill it")
                pos_input = int(input())
                if pos_input >= 0 and pos_input < len(empty_positions):
                    r , c = empty_positions[pos_input]
                    print("enter the Number to be filled in the position")
                    user_input = int(input())
                    state[r][c] = user_input
                    display(state)
                    empty_positions.remove([r,c])
                else:
                    print("Not a valid position !! Try again")
    return state
        
def end_game(sudoku_state,user_state):
    if sudoku_state == user_state:
        print("Congratulations !! You Won")
    else:
        print("You Failed !! play again")
        
def sudoku():
    grid_size , sudoku_state = initialize()
    user_state = list(map(list,sudoku_state))
    start_game(user_state)
    end_game(sudoku_state,user_state)
sudoku()
    


