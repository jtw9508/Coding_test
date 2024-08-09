import sys
n = int(sys.stdin.readline())

def recursive_answer(n, cnt):
    if n == cnt:
        print('____'*n + '"재귀함수가 뭔가요?"')
        print('____'*n + '"재귀함수는 자기 자신을 호출하는 함수라네"')    
    else:        
        a = '____'*(cnt)+'"재귀함수가 뭔가요?"'
        b = '____'*(cnt) +'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
        c = '____'*(cnt) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
        d = '____'*(cnt) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
        print(a)
        print(b)
        print(c)
        print(d)
        recursive_answer(n, cnt+1)
    print('____'*cnt + '라고 답변하였지.')

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursive_answer(n,0)

# n = int(input())
# def recur(n):
#     if n > 0:
#         recur(n-1)
#         print(n)
#         recur(n-2)

# def recur_w(n):
#     while n > 0:
#         recur_w(n-1)
#         print(n)
#         n -= 2

# recur_w(n)
# def reverse_str(c):
#     if len(c) == 1:
#         return c
#     return reverse_str(c[1:]) + c[0]
# print(reverse_str(string))

# def merge_sorted_list(list1, list2):
#     if not(len(list1)) or not(len(list2)):
#         return list1 + list2
#     else:
#         if list1[0] < list2[0]:
#             return [list1[0]] + merge_sorted_list(list1[1:], list2)
#         else:
#             return [list2[0]] + merge_sorted_list(list1,list2[1:])
# a = merge_sorted_list([1,3,4,5],[2,6,8,9])
# print(a)