import sys
input = sys.stdin.readline
N, M = map(int, input().split())

tree_list = list(map(int, input().split()))
start = 0
end = max(tree_list)
answer = 0
while start <= end:
    half = (start + end) // 2
    total = 0
    for tree in tree_list:
        if tree - half > 0:
            total += (tree - half)
    if total == M:
        answer = half
        break
    if total > M:
        start = half + 1
        answer = max(answer, half)
    else:
        end = half - 1
print(answer)

# ##내 꺼 .. 경계조건 처리가 쉽지 않음 아래의 코드는 min_height와 max_height가 같아졌을 때, max_height를 리턴할지 더 작은 height를 리턴할지 결정
# import sys
# N, M = map(int, sys.stdin.readline().split())
# tree_list = list(map(int, sys.stdin.readline().split()))
# tree_list

# def calculate_height(list, height):
#     total_tree = 0
#     for tree in list:
#         if tree - height > 0:
#             total_tree += tree - height
#     return total_tree


# def get_height(list, min_height, height):
#     if min_height >= height:
#         if calculate_height(tree_list, height) >= M:
#             return height
#         else:
#             return height - 1
#     else:
#         half = (min_height + height) // 2
#         total_tree = calculate_height(tree_list, half)
#         if total_tree == M:
#             return half
#         elif total_tree < M:
#             return get_height(list, min_height, half-1)
#         else:
#             return get_height(list, half+1, height)

# answer = get_height(tree_list,0,max(tree_list))
# print(answer)

# ##GPT 꺼
# import sys

# N, M = map(int, sys.stdin.readline().split())
# tree_list = list(map(int, sys.stdin.readline().split()))

# def calculate_height(list, height):
#     total_tree = 0
#     for tree in list:
#         if tree > height:
#             total_tree += tree - height
#     return total_tree

# def get_height(list, min_height, max_height):
#     while min_height <= max_height:
#         mid = (min_height + max_height) // 2
#         total_tree = calculate_height(list, mid)
        
#         if total_tree == M:  # 정확히 M만큼의 나무를 얻었을 때
#             return mid
#         elif total_tree < M:  # 더 적게 얻었다면, 높이를 낮춰서 더 많이 자르도록 한다
#             max_height = mid - 1
#         else:  # 더 많이 얻었다면, 높이를 높여서 덜 자르도록 한다
#             min_height = mid + 1

#     # 여기서 max_height는 M을 만족하는 가장 높은 절단 높이가 된다.
#     return max_height

# answer = get_height(tree_list, 0, max(tree_list))
# print(answer)