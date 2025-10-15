
board = [[' ' for _ in range(3)]for _ in range(3) ]
mark1, mark2='X','O'
marker1_moves=[]
marker2_moves=[]
print('\n')
def print_board(board):
    for i, row in enumerate(board):
        row_display = []
        if i>0:
            print("---+---+---")
        for j, val in enumerate(row):
            row_display.append(val+' | ')
        print(' '+board[i][0]+' | '+ board[i][1]+' | '+ board[i][2])
   
def take_input(mark):
    x = int(input(f'choose the x position of your {mark} mark'))
    y = int(input(f'choose the y position of your {mark} mark'))
    
    return x,y
def play(board):
    win = False
    
    while not win:
      
        move=take_input(mark1)
        board[move[0]][move[1]]= mark1
        print_board(board)
        move=take_input(mark2)
        board[(move[0])][move[1]]= mark2
        print_board(board)
play(board)       