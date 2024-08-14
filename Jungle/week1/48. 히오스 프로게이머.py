import sys

input = sys.stdin.readline

N, K = map(int, input().split())

levels = []
for i in range(N):
    levels.append(int(input()))

start = min(levels)
end = min(levels) + K
team_level = start
while start <= end:
    half = (start + end) // 2
    total = 0
    
    for level in levels:
        if half - level > 0:
            total += half - level
    if total == K:
        team_level = half
        break
    if total > K:
        end = half - 1
    else:
        start = half + 1
        team_level = max(team_level,half)
        
print(team_level)

# import sys

# N, K = map(int, sys.stdin.readline().split())
# level_list = []
# for i in range(N):
#     level_list.append(int(sys.stdin.readline()))
# level_list.sort()

# total_sum = sum(level_list)
# rest = level_list[-1]*len(level_list) - total_sum

# def find_index(start,end, K):
#     while start <= end:
#         half = (start + end) // 2
#         rest_sum = level_list[half] * (half + 1) - sum(level_list[:half+1])
#         if rest_sum == K:
#             return half
#         elif rest_sum > K:
#             end = half - 1
#         else:
#             start = half + 1
    
#     if start > len(level_list) - 1:
#         return len(level_list) - 1
#     if end < 0:
#         return 0
    
#     if rest_sum > K:
#         return end
#     else:
#         return start - 1
    
# index = find_index(0, len(level_list)-1,K)
# if index == len(level_list) - 1:
#     print(level_list[-1]+ (K - rest)// len(level_list))
# elif index == 0:
#     print(level_list[0] + K)
# else:
#     print(level_list[index] + (K -level_list[index]*(index+1)+sum(level_list[:index+1]))//(index+1))


# ##백준 코드
# import sys

# n,k = map(int,input().split())

# h=[]
# for _ in range(n):
#     h.append( int(sys.stdin.readline()))

# start=min(h)
# end=start+k
# level=0
# while start<=end:
#     total = 0
#     mid = (start+end)//2
#     for value in h:
#         if value < mid:
#             total+= mid - value
#         if total > k:
#             break 
#     if total > k:
#         end=mid-1
  
#     else:
#         start=mid+1
#         level = max(mid,level)
        
        
# print(level)
