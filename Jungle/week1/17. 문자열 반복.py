num = int(input())
temp =[]
for i in range(num):
    n, char = input().split()
    result = ''
    for c in char:
        result += c*int(n)
    temp.append(result)
for i in temp:
    print(i)