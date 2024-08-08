x, y = map(int, input().split())
iter = int(input())
length = [0,x]
height = [0,y]
for i in range(iter):
    a, b = map(int, input().split())
    if a == 1:
        length.append(b)
    else:
        height.append(b)
length.sort()
height.sort()
l_temp = length[1] - length[0]
h_temp = height[1] - height[0]
for i in range(1,len(length)):
    l_temp = max(l_temp, length[i]- length[i-1])

for i in range(1,len(height)):
    h_temp = max(h_temp, height[i]- height[i-1])

print(l_temp*h_temp)