import sys
size = int(sys.stdin.readline())
board =[]
for i in range(size):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
white = 0
blue = 0

def is_onecolor(board, start_row, start_col, size):
    first = board[start_row][start_col]
    for i in range(start_row, start_row+size):
        for j in range(start_col,start_col+size):
            current = board[i][j]
            if first != current:
                return False
    return True

def devide(board, start_row, start_col, size):
    if is_onecolor(board, start_row, start_col, size):
        if board[start_row][start_col] == 1:
            global blue 
            blue += 1
        else:
            global white
            white += 1
        return
    else:
        devide(board, start_row, start_col, size//2)
        devide(board, start_row + size//2, start_col, size//2)
        devide(board, start_row, start_col + size//2, size//2)
        devide(board, start_row + size//2, start_col + size//2, size//2)

devide(board,0,0, len(board))
print(white)
print(blue)