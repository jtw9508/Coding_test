import sys

fac_num = int(sys.stdin.readline())
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(fac_num))