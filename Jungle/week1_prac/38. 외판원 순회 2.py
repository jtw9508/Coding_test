# import sys
# input = sys.stdin.readline
# N = int(input())
# costs = []
# for i in range(N):
#     costs.append(list(map(int,input().split())))
# visited = [False]*N
# answer = float('inf')
# def calculate(route):
#     route += [route[0]]
#     answer = 0
#     for i in range(len(route)-1):
#         if costs[route[i]][route[i+1]] > 0:
#             answer += costs[route[i]][route[i+1]]
#         else:
#             return float('inf')
#     return answer

# def circulate(route):
#     global answer
    
#     if len(route) == N:
#         temp = calculate(route)
#         answer = min(temp, answer)
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             circulate(route +[i])
#             visited[i] = False
# circulate([])
# print(answer)

import sys
input = sys.stdin.readline
N = int(input())
costs = []
for i in range(N):
    costs.append(list(map(int,input().split())))
visited = [False]*N
answer = float('inf')

def circulate(cnt, now_total, route):
    global answer
    if now_total > answer:
        return
    if cnt == N:
        if costs[route[-1]][route[0]]:
            answer = min(now_total+costs[route[-1]][route[0]], answer)
            return
        else:
            return
    for i in range(N):
        if len(route) >= 1:
            if not visited[i]:
                if costs[route[-1]][i]:
                    visited[i] = True
                    circulate(cnt+1,now_total+ costs[route[-1]][i],route +[i])
                    visited[i] = False
                else:
                    return
        else:
            if not visited[i]:
                visited[i] = True
                circulate(cnt+1,now_total,route +[i])
                visited[i] = False

circulate(0,0,[])
print(answer)