import sys















# def permutations(arr, r):
#     result = []

#     def permute(path, options):
#         if len(path) == r:  # r개의 원소를 다 선택한 경우
#             result.append(path)
#             return
        
#         for i in range(len(options)):
#             # 현재 원소를 선택하고, 남은 원소들로 재귀 호출
#             permute(path + [options[i]], options[:i] + options[i+1:])
    
#     permute([], arr)
#     return result

# n = int(sys.stdin.readline())
# select = int(sys.stdin.readline())
# temp = []
# numbers = []
# for i in range(n):
#     card = sys.stdin.readline().strip()
#     temp.append(card)
# result = permutations(temp, select)
# for i in result:
#     numbers.append(int(''.join(i)))
# print(len(set(numbers)))

