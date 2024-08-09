n = int(input())
temp = []
for i in range(n):
    a = int(input())
    temp.append(a)
temp.sort()
for i in temp:
    print(i)