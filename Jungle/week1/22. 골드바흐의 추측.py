import math

def is_prime(n):
    if n == 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

nums = int(input())
answer = []
for i in range(nums):
    num = int(input())
    start = int(num / 2)
    while True:        
        if is_prime(start) and is_prime(num-start):
            answer.append([start,num-start])
            break
        start -= 1

for i in answer:
    print(i[0], i[1])    