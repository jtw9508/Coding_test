import sys
input = sys.stdin.readline
count = int(input())
num_list = list(map(int,input().strip().split()))
operator = input().split()
operator_set = ''
for i in range(len(operator)):
    operator_set += str(i)*int(operator[i])

##연산자가 이미 계산한 연산자일 시 calculate 함수 실행 하지 않음
operate_complete = set()

##변수 초기화
max_num = -999999999999
min_num = 999999999999

#연산해서 min,max 갱신
def calculate(operators):
    global max_num
    global min_num
    temp = num_list[0]
    for i in range(len(operators)):
        if operators[i] == '0':
            temp += num_list[i+1]
        if operators[i] == '1':
            temp -= num_list[i+1]
        if operators[i] == '2':
            temp *= num_list[i+1]
        if operators[i] == '3':
            if temp < 0:
                temp = - (-temp // num_list[i+1])
            else:
                temp = temp // num_list[i+1]
    max_num = max(max_num, temp)
    min_num = min(min_num, temp)

def insert_operator(operators, operator_input, n):
    #연산자 갯수가 n(count-1)일 시 연산 실행
    if len(operators) == n:
        if operators not in operate_complete:
            calculate(operators)
            operate_complete.add(operators) ##연산 시행한 연산자는 operators에 저장
            return
    else:
        for i in range(len(operator_input)):
            insert_operator(operators + operator_input[i],operator_input[:i] + operator_input[i+1:],n) ##재귀호출로 모든 가능한 연산자 조합 구하기

insert_operator('',operator_set,count-1)
print(max_num)
print(min_num)