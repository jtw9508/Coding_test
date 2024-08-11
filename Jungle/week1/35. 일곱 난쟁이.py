import sys

height_list = []
for i in range(9):
    height = int(sys.stdin.readline())
    height_list.append(height)

target = sum(height_list) - 100
def search(i,j):
    if i >= 8:
        return None
    if j >= 9:
        return search(i+1, i+2)
    if height_list[i] + height_list[j] == target:
        return i, j
    return search(i, j+1)

i, j = search(0,1)
height_list.pop(j)
height_list.pop(i)
for height in sorted(height_list):
    print(height)
