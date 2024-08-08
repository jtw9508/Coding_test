A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
result_temp = [0]*10
for i in result:
    result_temp[int(i)] += 1
for i in result_temp:
    print(i)