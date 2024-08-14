import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = len(liquid) - 1
answer = float('inf')
answer_1, answer_2 = None, None
while left < right:
    current = liquid[left] + liquid[right]
    if abs(current) < abs(answer):
        answer = current
        answer_1, answer_2 = liquid[left], liquid[right]
    if current == 0:
        answer_1, answer_2 = liquid[left], liquid[right]
        break
    if current > 0:
        right -= 1
    else:
        left += 1
print(answer_1, answer_2) 






































##이진탐색
import sys

input = sys.stdin.readline
N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

def find_closest_sum_pair(liquid):
    closest_sum = float('inf')
    answer_1, answer_2 = None, None

    for i in range(N - 1):
        target = -liquid[i]
        left, right = i + 1, N - 1
        
        while left <= right:
            mid = (left + right) // 2
            current_sum = liquid[i] + liquid[mid]
            
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                answer_1, answer_2 = liquid[i], liquid[mid]
            
            if liquid[mid] == target:
                return answer_1, answer_2
            elif liquid[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return answer_1, answer_2

# 메인 로직
result = find_closest_sum_pair(liquid)
print(result[0], result[1])


##투 포인터
def solutiuon(N,sample):
    i = 0
    j = N-1
    answer = (9999999999,0)
    while i < j:
        if abs(answer[0]+answer[1]) > abs(sample[i]+sample[j]):
            answer = (sample[i],sample[j])
        if sample[i] + sample[j] == 0:
            return answer
        elif sample[i] + sample[j] < 0:
            i += 1
            continue
        elif sample[i] + sample[j] >0:
            j -= 1
    return answer
N = int(input())
sample = list(map(int,input().split()))
sample.sort()
print(' '.join(map(str,solutiuon(N,sample))))
            