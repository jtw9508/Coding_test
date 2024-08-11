import sys
board_size = int(sys.stdin.readline())
costs = []
for i in range(board_size):
    cost = list(map(int, sys.stdin.readline().rstrip().split()))
    costs.append(cost)
city = [i for i in range(board_size)]

answer = 99999999

def calculate(path):
    global answer
    temp = 0
    cir_path = path + [path[0]] ##마지막은 출발지점으로 돌아온다.
    for i in range(1,len(cir_path)):
        if costs[cir_path[i-1]][cir_path[i]] == 0: ##경로 중 못 가는 경우 계산을 종료
            return
        else:
            temp += costs[cir_path[i-1]][cir_path[i]]
    answer = min(answer, temp)
    print(answer)
    return

def circulate(path,search):
    if len(path) == board_size: ## 경로 후보 경우의 수를 찾았을 경우 경로 비용 계산
        print(path)
        calculate(path)
        return
    else:
        for i in range(len(search)):
            circulate(path + [search[i]],search[:i]+search[i+1:])

circulate([],city)
print(answer)
