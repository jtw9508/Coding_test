import sys
M, N, L = map(int, sys.stdin.readline().split())

point_list = list(map(int, sys.stdin.readline().split()))
point_list.sort()
answer = 0

def find_x(point, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if point[0] == point_list[mid]:
            return point_list[mid]
        elif point[0] < point_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    # 종료된 후, 가장 가까운 위치를 반환
    if start >= len(point_list):  # 범위를 초과한 경우
        return point_list[end]
    if end < 0:  # 범위보다 작은 경우
        return point_list[start]
    
    # 두 위치 중 더 가까운 위치를 반환
    if abs(point[0] - point_list[start]) < abs(point[0] - point_list[end]):
        return point_list[start]
    else:
        return point_list[end]

for i in range(N):
    animal = list(map(int, sys.stdin.readline().split()))
    closest_point = find_x(animal, 0, len(point_list) - 1)
    if abs(animal[0] - closest_point) + animal[1] <= L:
        answer += 1

print(answer)