n = int(input())


def hanoi(n, f, s, t):
    if n == 1:
        print(f, t)
    else:
        hanoi(n-1,f,t,s)
        print(f, t)        
        hanoi(n-1,s,f,t)
if n <= 20:
    print(2**n -1)
    hanoi(n,1,2,3)
else:
    print(2**n-1)

