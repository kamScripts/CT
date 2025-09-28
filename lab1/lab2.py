def create_grid(size: int,fill=0)->list:
    """
    Create size x size grid filled with 0 as default
    size: int, grid size
    fill: item of the inner list
    
    Returns: 2-dimensional list of int.    
    """
    arr=[]
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append(str(fill))
    return arr
for row in create_grid(10):
    print("  ".join(row))