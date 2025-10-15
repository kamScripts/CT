import array

## Generate the 1d array. This is the quick and dirty method.
my_grid = array.array('i', [0 for _ in range(1000)])
## Ideally we should have width and height before creating the array
## Its ok in this instance, but does not scale well. 
width = 10
print(len(my_grid)//2)

## Loop through the array
for index in range(len(my_grid)):
    # Y is the integer division of the index
    y = index//width
    # X is the index modulo width
    x = index % width
    if not x: # print a new line at x = 0
        print()
    # This long conditional allows x to be printed around the edges
    
    if (x == 0 or y == 0) or (x == width-1 or y == width - 1) :
        print("X", end=' ')
    #middle element
    elif ((x== width//2 and y==width//2) or (x== width//2 and y==width//2-1)):
        print("X", end=' ')
    #middle-1 element
    elif ((x== width//2-1 and y==width//2-1) or (x== width//2-1 and y==width//2)):
        print("X", end=' ')
    
    else:
        # Anything inside these edges appears as 0.
        print(0, end=' ')
    