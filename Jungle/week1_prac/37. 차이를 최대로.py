# import sys
# input = sys.stdin.readline

# N = int(input())
# num_list = list(map(int, input().split()))
# index_list = [i for i in range(N)]
# is_used = [False] * N
# answer = 0
# def calculate(list):
#     answer = 0
#     for i in range(1,N):
#         answer += abs(num_list[list[i]]-num_list[list[i-1]])
#     return answer
# def maximize(list):
#     global answer
#     if len(list) == N:
#         # print(list)
#         if calculate(list) == max(answer,calculate(list)):
#             answer = max(answer,calculate(list))
#             print(list)
        
#         return
#     for i in range(N):
#         if not is_used[i]:
#             is_used[i] = True
#             maximize(list + [index_list[i]])
#             is_used[i] = False
# maximize([])
# print(answer)

import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
index_list = [i for i in range(N)]
is_used = [False] * N
answer = 0
def calculate(list):
    answer = 0
    for i in range(1,N):
        answer += abs(num_list[list[i]]-num_list[list[i-1]])
    return answer

def maximize(list,search):
    global answer
    if len(list) == N:
        answer = max(answer,calculate(list))
        return
    for i in range(len(search)):
        maximize(list + [search[i]], search[:i]+ search[i+1:])

maximize([],index_list)
print(answer)
