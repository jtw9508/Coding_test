import sys
N, best_sum = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
def blackjack(cnt,start,temp, best_sum):
    if cnt == 3: ##base_case
        if temp <= best_sum:
            global answer
            answer = max(temp, answer)
        return
    
    for i in range(start, N):
        blackjack(cnt+1,i+1, temp + cards[i],best_sum)
blackjack(0,0,0,best_sum)
print(answer)
    
    

