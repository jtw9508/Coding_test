i, max = 0, 0
for index in range(9):
    temp = int(input())
    if max < temp:
        i = index+1
        max = temp
print(max)
print(i)
