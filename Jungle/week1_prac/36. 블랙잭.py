##완전 탐색
# import sys
# input = sys.stdin.readline
# N, M = map(int,input().split())

# card_list = list(map(int, input().split()))
# selected = [False]*len(card_list)
# answer = 0
# def blackjack(cnt, list,cards):
#     global answer
#     if cnt == 3:
#         if sum(list) <= M:
#             answer = max(sum(list),answer)
#         return
#     else:
#         for i in range(len(card_list)):
#             if not selected[i]:
#                 selected[i] = True
#                 blackjack(cnt+1, list + [card_list[i]],cards[:i]+ cards[i+1:])
#                 selected[i] = False
# blackjack(0,[], card_list)
# print(answer)

# ##조합
# import sys
# input = sys.stdin.readline
# N, M = map(int,input().split())

# card_list = list(map(int, input().split()))
# answer = 0
# def blackjack(cnt, start, list):
#     global answer
#     if cnt == 3:
#         if sum(list) <= M:
#             answer = max(sum(list),answer)
#         return
#     else:
#         for i in range(start,len(card_list)):
#             list.append(card_list[i])
#             blackjack(cnt+1, i+1, list)
#             list.pop()

# blackjack(0,0,[])
# print(answer)

##최적화
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

card_list = list(map(int, input().split()))
answer = 0
def blackjack(cnt, start, temp):
    global answer
    if cnt == 3:
        if temp <= M:
            answer = max(temp,answer)
        return
    else:
        for i in range(start,len(card_list)):
            temp += card_list[i]
            blackjack(cnt+1, i+1, temp)
            temp -= card_list[i]


blackjack(0,0,0)
print(answer)