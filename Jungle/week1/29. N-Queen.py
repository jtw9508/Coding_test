# N = int(input())
# board = [[0]*N for _ in range(N)]
# board_can_locate = [[False] * N for _ in range(N)]
# def N_Queen(N, start):
#     if start == N:
#         for i in range(len(board_can_locate[N])):
#             if board_can_locate[N][i]:
#                 board[N][i] == 1
#     else:

def is_safe(row, col, board_can_locate):
    # 같은 열에 다른 퀸이 있는지 확인
    for i in range(row):
        if not board_can_locate[i][col]:
            return False
    
    # 왼쪽 대각선에 다른 퀸이 있는지 확인
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if not board_can_locate[i][j]:
            return False

    # 오른쪽 대각선에 다른 퀸이 있는지 확인
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board_can_locate))):
        if not board_can_locate[i][j]:
            return False

    return True
answer = 0
def solve_n_queens(N, row, board, board_can_locate):
    
    if row == N:
        # 모든 행에 퀸을 배치한 경우, 결과를 출력
        global answer
        answer += 1
        print(answer)
        # for line in board:
        #     print(line)

        # print()
        return

    for col in range(N):
        if is_safe(row, col, board_can_locate):
            # 퀸을 현재 위치에 배치
            board[row][col] = 1
            # 이 위치를 사용할 수 없도록 표시
            board_can_locate[row][col] = False

            # 다음 행에 대해 재귀적으로 해결
            solve_n_queens(N, row + 1, board, board_can_locate)

            # 백트래킹: 퀸을 제거하고, 다시 이전 상태로 되돌림
            board[row][col] = 0
            board_can_locate[row][col] = True
    return answer
N = int(input())
board = [[0] * N for _ in range(N)]
board_can_locate = [[True] * N for _ in range(N)]
a = solve_n_queens(N, 0, board, board_can_locate)
print(a)
