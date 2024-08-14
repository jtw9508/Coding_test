import sys

input = sys.stdin.readline
n = int(input())
num_list = list(map(int,input().split()))
operators = list(map(int,input().split()))
min_num = float('inf')
max_num = float('-inf')
def calculate(operator_list):
    temp = num_list[0]
    for i, v in enumerate(operator_list):
        if v == 0:
            temp += num_list[i+1]
        elif v == 1:
            temp -= num_list[i+1]
        elif v == 2:
            temp *= num_list[i+1]
        elif v == 3:
            if temp < 0:
                temp = -(-temp // num_list[i+1])
            else:
                temp = temp // num_list[i+1]
    return temp

def get_operator(operator_list):
    global min_num
    global max_num

    if len(operator_list) == len(num_list)-1: ##base case
        temp = calculate(operator_list)
        min_num = min(min_num, temp)
        max_num = max(max_num, temp)
        return
    
    for i in range(len(operators)):
        if operators[i] > 0:
            operators[i] -= 1
            get_operator(operator_list + [i])
            operators[i] += 1

get_operator([])
print(max_num)
print(min_num)