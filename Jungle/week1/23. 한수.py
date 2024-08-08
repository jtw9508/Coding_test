num = int(input())
if num < 100:
    print(num)
else:
    answer = 99
    for i in range(100, num+1):
        if (i%10) - ((i//10)%10) == ((i//10)%10) - (i//100):
            answer += 1
    print(answer)
