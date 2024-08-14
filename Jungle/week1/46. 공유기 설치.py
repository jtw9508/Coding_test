import sys

N, C = map(int, sys.stdin.readline().split())
house = []
for i in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()

def set_x(list):
    min_num = 1
    max_num = list[-1] - list[0]
    answer = 0
    while min_num <= max_num:
        half = (min_num + max_num) // 2
        cnt = 1
        prev = list[0]
        for i in range(1,len(list)):
            if list[i] - prev >= half:
                cnt += 1
                prev = list[i]
        if cnt >= C:
            answer = max(answer, half)
            min_num = half + 1
        else:
            max_num = half - 1
    return answer

print(set_x(house))

