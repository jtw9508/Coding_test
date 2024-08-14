import sys
input = sys.stdin.readline
heights = []
for i in range(9):
    heights.append(int(input()))
target = sum(heights) - 100
is_cal = [False] * len(heights)

def find_height(cnt,list):
    if cnt == 2:
        if sum(list) == target:
            return list
        else:
            return None
    else:
        for i in range(len(heights)):
            if not is_cal[i]:
                is_cal[i] = True
                result = find_height(cnt + 1, list +[heights[i]])
                is_cal[i] = False
                if result is not None:
                    return result
    return None
except_list = find_height(0,[])
answer = [i for i in heights if i not in except_list]
answer.sort()
for i in answer:
    print(i)
