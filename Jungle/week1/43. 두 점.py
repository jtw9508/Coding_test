import sys
input = sys.stdin.readline

n = int(input())
point_list_all = []
for i in range(n):
    x, y = map(int, input().split())
    point_list_all.append((x,y))

answer = float('inf')

def point_check(point_list,a,b,c,d):
    result = []
    for point in point_list:
        if (point[0] >= a and point[0] <= b) and (point[1] >= c and point[1] <= d):
            result.append(point)
    return result

def point_list_check(point_list, a, b, c, d, size):
    global answer
    point_list_check = point_check(point_list, a, b, c, d)
    if len(point_list_check) == 0:
        return
    if len(point_list_check) == 1:
        for point in point_list:
            temp = (point_list_check[0][0]-point[0])**2 + (point_list_check[0][1]-point[1])**2
            if temp > 0:
                answer = min(answer, temp)
        return
    else:
        min_point(point_list_check, a,b,c,d, size)

def min_point(point_list, a, b, c, d, size):
    global answer
    if len(point_list) == 0:
        return
    if len(point_list) == 1:
        for i in point_list_all:
            temp = (point_list[0][0]-i[0])**2 + (point_list[0][1]-i[1])**2
            if temp > 0:
                answer = min(answer, temp)
        return 
    if len(point_list) == 2:
        length = (point_list[0][0] -point_list[1][0])**2 + (point_list[0][1] -point_list[1][1])**2
        answer = min(answer,length)
        return
    else:
        size = size / 2
        point_list_check(point_list,a,b-size,c,d-size, size)
        point_list_check(point_list,a+size,b,c,d-size, size)
        point_list_check(point_list,a,b-size,c+size,d, size)
        point_list_check(point_list,a+size,b,c+size,d, size)

if len(point_list_all) != len(set(point_list_all)):
    answer = 0
else:
    min_point(point_list_all,-10000,10000,-10000,10000,20000)
print(answer)