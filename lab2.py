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
    for r in arr:
        print("  ".join(map(str, r)))
    print("\n")


if __name__ == "__main__":
    grid=create_grid(10)
    increment_grid_item(grid,0,0)
    display_grid(grid)
    print(id(grid[0]), id(grid[1]), id(grid[2]))
    # solution from the presentation
    rows,cols=10,10
    #matrixConst = list([[0] * 10] * 10)
    #matrixRange = [list(range(10))] *10
    matrixCompr = [[0 for _ in range(cols)] for _ in range(rows)]
    display_grid(matrixCompr)
    print(id(matrixCompr[0]), id(matrixCompr[1]), id(matrixCompr[2]))    