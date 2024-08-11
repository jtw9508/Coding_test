# N = int(input())
# board = [[0]*N for _ in range(N)]
# board_can_locate = [[False] * N for _ in range(N)]
# def N_Queen(N, start):
#     if start == N:
#         for i in range(len(board_can_locate[N])):
#             if board_can_locate[N][i]:
#                 board[N][i] == 1
#     else:

# def is_safe(row, col, board_can_locate):
#     # 같은 열에 다른 퀸이 있는지 확인
#     for i in range(row):
#         if not board_can_locate[i][col]:
#             return False
    
#     # 왼쪽 대각선에 다른 퀸이 있는지 확인
#     for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
#         if not board_can_locate[i][j]:
#             return False

#     # 오른쪽 대각선에 다른 퀸이 있는지 확인
#     for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board_can_locate))):
#         if not board_can_locate[i][j]:
#             return False

#     return True
# answer = 0
# def solve_n_queens(N, row, board, board_can_locate):
    
#     if row == N:
#         # 모든 행에 퀸을 배치한 경우, 결과를 출력
#         global answer
#         answer += 1
#         print(answer)
#         # for line in board:
#         #     print(line)

#         # print()
#         return

#     for col in range(N):
#         if is_safe(row, col, board_can_locate):
#             # 퀸을 현재 위치에 배치
#             board[row][col] = 1
#             # 이 위치를 사용할 수 없도록 표시
#             board_can_locate[row][col] = False

#             # 다음 행에 대해 재귀적으로 해결
#             solve_n_queens(N, row + 1, board, board_can_locate)

#             # 백트래킹: 퀸을 제거하고, 다시 이전 상태로 되돌림
#             board[row][col] = 0
#             board_can_locate[row][col] = True
#     return answer
# N = int(input())
# board = [[0] * N for _ in range(N)]
# board_can_locate = [[True] * N for _ in range(N)]
# a = solve_n_queens(N, 0, board, board_can_locate)
# print(a)

# pos = [0]*8

# def put():
#     for i in range(8):
#         print(pos[i], end = '')
#     print()

# def set(i):
#     for j in range(8):
#         pos[i] = j
#         if i ==7:
#             put()
#         else:
#             set(i+1)


# #스택에 값을 저장하고 pos에 업데이트하여 모든 퀸의 가능한 가짓수를 계산하는 방법
# pos = [0] * 8
# def put():
#     for i in range(8):
#         print(pos[i], end='')
#     print()

# def set_iterative():
#     stack = [0] * 8  # 각 위치의 값들을 관리하는 스택
#     i = 0  # 현재 조작 중인 인덱스
#     while i >= 0:
#         if stack[i] < 8:
#             pos[i] = stack[i] #pos에 값을 업데이트(해당 열 어떤 행에 퀸을 놓을지)
#             stack[i] += 1 #pos를 업데이트한 후 stack의 값(다음 행에 퀸을 놓는 경우의 수) 업데이트

#             if i == 7: #만약에 i가 마지막 열의 queen을 놓은 경우, 8개의 퀸을 다 놓은 상태이기 때문에 출력
#                 put()
#             else: #queen을 다 놓지 않은 경우, 다음 열에 queen배치
#                 i += 1
#         else:
#             stack[i] = 0 #끝까지 행을 다 놓은 경우 0으로 리셋 후 이전 열로 다시 돌아가기
#             i -= 1

# set_iterative()


# pos = [0]*3
# flag = [False] * 3

# def put():
#     for i in range(3):
#         print(pos[i], end = '')
#     print()

# def set(i):
#     for j in range(3):
#         if not flag[j]:        
#             pos[i] = j            
#             if i == 2:
#                 put()
#             else:
#                 flag[j] = True
#                 set(i+1)
#                 flag[j] = False
# set(0)

##백트래킹 알고리즘 Pseudo code
# def promising(v): ##하위 노드에 답이 있을까?
#     if v >10:
#         return True
#     return False

# def checknode(v):
#     if promising(v): ##하위 노드에 답이 있을 가능성이 있다면? -> 탐색
#         if v ==100: ##v가 해답이라면
#             print(v)
#         else: ##해답이 아니라면 v의 자식 노드로 이동해서 다시 체크를 반복
#             checknode(v+1) 

def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

def n_queens(i, col):
    n = len(col) - 1
    if (promising(i, col)):
        if (i ==n):
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i+1, col)
n = 4
col = [0]* (n+1)
n_queens(0, col)

