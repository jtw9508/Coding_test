# import sys

# N, r, c = map(int,sys.stdin.readline().split())
# board = [[0]*2**N for _ in range(2**N)]

# def z(board,start_row, start_col, size, k):
#     if size == 2:
#         board[start_row][start_col] += k
#         board[start_row][start_col+1] += k+1
#         board[start_row+1][start_col] += k+2
#         board[start_row+1][start_col+1] += k+3
#     else:
#         size = size//2
#         x = 2**(size)
#         z(board,start_row,start_col, size, k)
#         z(board,start_row,start_col + size, size, k + x )
#         z(board,start_row + size,start_col , size, k + 2*x )
#         z(board,start_row + size,start_col + size, size, k + 3*x )
# z(board,0,0,len(board),0)
# # print(board)
# print(board[r][c])

import sys

N, r, c = map(int, sys.stdin.readline().split())

def z(n, x, y):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    if r < x + half and c < y + half:
        # 좌상단
        return z(n-1, x, y)
    elif r < x + half and c >= y + half:
        # 우상단
        return half * half + z(n-1, x, y + half)
    elif r >= x + half and c < y + half:
        # 좌하단
        return 2 * half * half + z(n-1, x + half, y)
    else:
        # 우하단
        return 3 * half * half + z(n-1, x + half, y + half)

print(z(N, 0, 0))
