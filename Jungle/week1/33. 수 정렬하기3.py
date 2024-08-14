import sys
N = int(sys.stdin.readline())

num_set = {}
for i in range(N):
    n = int(sys.stdin.readline())
    if n not in num_set:
        num_set[n] = 1
    else:
        num_set[n] += 1

keys = sorted(list(num_set.keys()))

for key in keys:
    for i in range(num_set[key]):
        print(key)