# import sys

# fac_num = int(sys.stdin.readline())
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(fac_num))

def fac(n, count):
    if n < 2:
        return count
    return fac(n-1, n*count)

print(fac(5, 1))