import math

def is_prime(n):
    if n == 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
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

#######################################################
def isPrime(n):
  for i in range(2,(n//2)+1):
    if n%i == 0:
      return False
  return True

T = int(input())
answer = []
for i in range(T):
  a = int(input())
  check = int(a/2)
  if a == 4:
    answer.append([2,2])
    continue
  if check%2 ==0:
    for j in range(check-1,0,-2):
      if isPrime(j) and isPrime(a-j):
        answer.append([j,a-j])
        break
  else:
    for j in range(check,0,-2):
      if isPrime(j) and isPrime(a-j):
        answer.append([j,a-j])
        break
for i in answer:
  print(i[0],i[1])