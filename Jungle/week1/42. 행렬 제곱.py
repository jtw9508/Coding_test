import sys
N, B = map(int,sys.stdin.readline().split())
matrix = []
for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    matrix.append(row)

def mul(matrix1, matrix2):
    result = []
    rows, cols = len(matrix1), len(matrix1)
    for row in range(rows):
        row_temp = []
        for col in range(cols):
            temp = 0
            for i in range(cols):
                temp += matrix1[row][i]*matrix2[i][col]
            row_temp.append(temp%1000)
        result.append(row_temp)
    return result

def matrix_sqrt(matrix_result, matrix_input, B):
    if B == 1:
        return mul(matrix_result,matrix_input)
    else:
        matrix_result = matrix_sqrt(matrix_result, matrix_input, B//2)
        matrix_result = mul(matrix_result,matrix_result)
        if B%2 == 0:
            return matrix_result
        else:
            return mul(matrix_result,matrix_input)
        
initial_matrix = [[0]*N for _ in range(N)]
# print(initial_matrix)
for i in range(N):
    initial_matrix[i][i] = 1
    
answer = matrix_sqrt(initial_matrix,matrix,B)
for i in answer:
    print(" ".join(map(str, i)))

