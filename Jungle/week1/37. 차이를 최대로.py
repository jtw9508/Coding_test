import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
def calculate_sum(list):
    temp = 0
    for i in range(1,len(list)):
        temp += abs(list[i] - list[i-1])
    return temp
    

def search_list(list,list_search,n):
    global answer
    if len(list) == n: ##n개를 다 선택한 경우 합을 구하기(base case)
        temp = calculate_sum(list)
        answer = max(answer, temp)
    else:
        for i in range(len(list_search)):
            search_list(list + [list_search[i]],list_search[:i]+list_search[i+1:], n) ##n개를 선택하지 않은 경우 다음 숫자 선택

search_list([],num_list,len(num_list))
print(answer)