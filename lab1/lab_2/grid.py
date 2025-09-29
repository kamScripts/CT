import keyboard
import os
from termcolor import colored, cprint


rows,cols=10,10
grid = [[0 for _ in range(cols)] for _ in range(rows)]
grid[0][0]=1
x,y=0,0

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def create_grid(size: int,fill:int=0)->list:
    """
    Create size x size grid filled with 0 as default.
    
    size: int, grid size
    fill: item of the inner list
    
    Returns: 2-dimensional list of int items.    
    """
    arr=[]
    for i in range(size):
        arr.append([])
        for _ in range(size):
            arr[i].append(fill)
    return arr
def increment_grid_item(arr:list[int],row:int,col:int, inc:bool=True)->None:
    """
    Increment/ decrement grid item at [row,index].
    
    arr: list[str], a grid
    row: int, outer list index
    col: int, inner list index
    incr: bool, Equation symbol
    
    Returns: None
    """
    if inc:
        arr[row][col]+=1
    else:
        arr[row][col] -=1
def display_grid(arr:list)->None:
    """
    Print 2-d list
    arr: list of any type
    Returns: None
    """
    global x,y
    clear_terminal()
    for i, row in enumerate(arr):
        row_display = []
        for j, val in enumerate(row):
            if i == x and j == y:
                row_display.append(colored(str(val), 'light_green'))
            else:
                row_display.append(str(val))
        print("  ".join(row_display))
    print("\n")


def arrow_up(grid, row,col):
    if row==0:
        increment_grid_item(grid,-1,col)
        increment_grid_item(grid,row,col, inc=False)
        
    else:
        increment_grid_item(grid,row-1,col)
        increment_grid_item(grid,row,col, inc=False)
        
def arrow_down(grid, row, col):
    if row == len(grid) - 1:
        increment_grid_item(grid, 0, col)
        increment_grid_item(grid, row, col, inc=False)
    else:
        increment_grid_item(grid, row + 1, col)
        increment_grid_item(grid, row, col, inc=False)

def arrow_left(grid, row, col):
    if col == 0:
        increment_grid_item(grid, row, -1)
        increment_grid_item(grid, row, col, inc=False)
    else:
        increment_grid_item(grid, row, col - 1)
        increment_grid_item(grid, row, col, inc=False)

def arrow_right(grid, row, col):
    if col == len(grid[0]) - 1:
        increment_grid_item(grid, row, 0)
        increment_grid_item(grid, row, col, inc=False)
    else:
        increment_grid_item(grid, row, col + 1)
        increment_grid_item(grid, row, col, inc=False)



def on_key_up(event)->None:
    global grid, x, y   
    match event.name:
        case "up":
            arrow_up(grid, x, y)
            x = 9 if x == 0 else x - 1
            display_grid(grid)
        case "down":
            arrow_down(grid, x, y)
            x = 0 if x == len(grid) - 1 else x + 1
            display_grid(grid)
        case "left":
            arrow_left(grid, x, y)
            y = 9 if y == 0 else y - 1
            display_grid(grid)
        case "right":
            arrow_right(grid, x, y)
            y = 0 if y == len(grid[0]) - 1 else y + 1
            display_grid(grid)
        case _:
            print("press the arrow keys or esc")

def main():
    for key in ['up', 'down', 'left', 'right']:
        keyboard.on_release_key(key, on_key_up)
        
    keyboard.wait('esc')


if __name__ == "__main__":
    display_grid(grid)
    main()